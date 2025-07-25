

type RGB = [number, number, number];
const acanvas = document.getElementById("#alice");
if (!(acanvas instanceof HTMLCanvasElement)) {
  throw new Error("Alice canvas not found.");
}

const bcanvas = document.getElementById("#bob");
if (!(bcanvas instanceof HTMLCanvasElement)) {
  throw new Error("Bob canvas not found.");
}

const palette = document.querySelector(`input[type="color"]`);
if (!(palette instanceof HTMLInputElement)) {
  throw new Error("Pallette input not found.");
}

const artboard = {w:1000, h:1000};

const alice = PixelEditor(acanvas, artboard);
const bob = PixelEditor(bcanvas, artboard);

alice.onchange = state => {
  bob.setState(state);
}

bob.onchange = state => {
  alice.setState(state);
}

palette.oninput = (e) => {
    const hex = palette.value.substring(1).match(/[\da-f]{2}/g) || [];
    const rgb = hex.map(x => parseInt(x, 16));
    if (rgb.length === 3) {
      alice.color = bob.color = rgb as RGB;
    }
}