import ctypes
from typing import Dict,List, Callable,TypeVar
import math
from Pillow import Image
import numpy as np

from CRDTs import RGB, PixelData
HTMLCanvasElement = TypeVar('HTMLCanvasElement')
CanvasRederingContext2D = TypeVar('CanvasRederingContext2D')
class PixelEditor:
    el : HTMLCanvasElement
    ctx : CanvasRederingContext2D
    artboard: Dict[str:int]
    data = PixelData()
    color : RGB
    listeners: List[Callable[[PixelData.state],None]] = []

    def __init__(self, el: HTMLCanvasElement,artboard:  Dict[str:int]):
        self.el = el
        self.artboard= artboard

        ctx = el.getContext("2d")
        if not ctx:
            raise Exception("couldn't get rendering context")
        self.ctx = ctx

        self.color = RGB(0,0,0)

        self.el.addEventListener("pointerdown", self.handle_event)
        self.el.addEventListener("pointermove", self.handle_event)
        self.el.addEventListener("pointerup", self.handle_event)

        device_pixel_ratio = 1  # Replace with the actual device pixel ratio if available
        self.el.width = self.clientWidth * device_pixel_ratio
        self.el.height = self.clientHeight * device_pixel_ratio
        try:
            # Attempt to get the device pixel ratio using ctypes for Windows
            user32 = ctypes.windll.user32
            user32.SetProcessDPIAware()
            device_pixel_ratio = user32.GetDpiForWindow(self.el.hWnd) / 96.0
        except AttributeError:
            # Fallback if ctypes or specific attributes are not available
            device_pixel_ratio = 1

        self.el.width = int(self.el.clientWidth * device_pixel_ratio)
        self.el.height = int(self.el.clientHeight * device_pixel_ratio)            
        self.ctx.scale(device_pixel_ratio, device_pixel_ratio)

    def on_change(self, listener: Callable[[PixelData.state],None])->None:
        """
        Adds a listener for changes in PixelData state.
        :param listener: A callable that takes the state of PixelData as an argument.
        """
        self.listeners.append(listener)

    def set_color (self,color : RGB):
        self.color = color

    def handle_event(self, e: "PointerEvent") -> None:
        """
        Handles events on the canvas.
        :param e: Pointer event from the canvas element.
        """
        if e.type == "pointerdown":
            self.el.setPointerCapture(e.pointerId)
            
        elif e.type == "pointermove":
            if not self.el.hasPointerCapture(e.pointerId):
                return
            
            x = math.floor(self.artboard['w'] * e.offsetX / self.el.clientWidth * self.el.width)
            y = math.floor(self.artboard['h'] * e.offsetY / self.el.clientHeight * self.el.height)
            self.paint(x,y)
        elif e.type == "pointerup":
            self.el.releasePointerCapture(e.pointerId)
    def notify_change(self, state: PixelData.state) -> None:
        """
        Notifies all registered listeners of a change in PixelData state.
        :param state: The new state of PixelData.
        """
        for listener in self.listeners:
            listener(state)

    def paint(self,x,y):
        """* Sets pixel under the mouse cursor with the current color.
   * @param x X coordinate of the destination pixel.
   * @param y Y coordinate of the destination pixel.
        """
        if x < 0 or y < 0 or x >= self.el.width or y >= self.el.height:
            return
        self.data.set(x,y,self.color)
        self.draw()
        self.notify_change(self.data.state)

    def draw(self):
        """* Draws the current state of the PixelData onto the canvas.
        """
        #number of channels per pixel: R,G,B,A
        channels = 4
        """
        A buffer to hold the raw pixel data.
     * Each pixel corresponds to four bytes in the buffer,
     * so the full size is the number of pixels times the number of channels per pixel. 
        """
        buffer = (ctypes.c_uint8 * (self.artboard['w'] * self.artboard['h'] * channels))()
        #The number of bytes in the buffer representing a single artboard row. */
        rowsize = self.artboard['w']

        for row in range(self.artboard['h']):
            #calculate the byte offset of the start of the row relative to the start of the buffer
            offsetY = row * rowsize
            for col in range(self.artboard['w']):
                #calculate the byte offset of the pixel relative to the start of the row
                offetX = col * channels
                #calculate the byte offset of the pixel relative to the start of the buffer
                offset = offsetY + offetX
                r,g,b = self.data.get(col,row)
                buffer[offset] = r
                buffer[offset + 1] = g
                buffer[offset + 2] = b
                buffer[offset + 3] = 255
        data =self.ctx.putImageData(self.ctx.createImageData(self.artboard['w'], self.artboard['h']), 0, 0)
       

        # Convert buffer to a NumPy array and reshape it to (height, width, channels)
        pixel_array = np.frombuffer(buffer, dtype=np.uint8).reshape((self.artboard['h'], self.artboard['w'], channels))
        
        # Create an image using Pillow
        bitmap = Image.fromarray(pixel_array, 'RGBA')
        
        # Draw the image onto the canvas
        self.ctx.drawImage(bitmap, 0, 0, self.el.width, self.el.height)


    
    def receive(self,state: PixelData.state):
        """
            * Merge remote state with the current state and redraw the canvas.
    * @param state State to merge into the current state.
        """
        self.data.merge(state)
        self.draw()
        self.notify_change(self.data.state)

        
