from typing import NamedTuple

class RGB(NamedTuple):
    red: int
    green: int
    blue: int


class RGBColor:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def to_rgb(self) -> RGB:
        return RGB(self.red, self.green, self.blue)
    
    def __str__(self) -> str:
        return f"RGB({self.red}, {self.green}, {self.blue})"
    
    def __repr__(self) -> str:
        return f"RGBColor({self.red}, {self.green}, {self.blue})"
