#!/usr/bin/python
from rgbmatrix import graphics
import time
from PIL import Image
from PIL import ImageDraw
from rgbmatrix import RGBMatrix, RGBMatrixOptions


# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 2
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  

matrix = RGBMatrix(options = options)
font = graphics.Font()
font.LoadFont("../../../fonts/8x13B.bdf")
offscreen_canvas = matrix.CreateFrameCanvas()

#Colors
green = graphics.Color(0,150,0)
red = graphics.Color(150,0,0)
purple = graphics.Color(255,0,255)

while True:
    current_time = time.strftime("%I:%M")
    ampm = time.strftime("%p")
   
#Clock Face:
    graphics.DrawText(offscreen_canvas, font, 2, 20, red, current_time)
    graphics.DrawText(offscreen_canvas, font, 47, 20, green, ampm)
    offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
    
    time.sleep(0.25)

    offscreen_canvas.Clear() 
