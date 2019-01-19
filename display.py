import RPi.GPIO as GPIO
from rgbmatrix import graphics
import time
from PIL import Image
from PIL import ImageDraw
from rgbmatrix import RGBMatrix, RGBMatrixOptions

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 2
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

#some variables
matrix = RGBMatrix(options = options)
font = graphics.Font()
font.LoadFont("../../../fonts/8x13B.bdf")
offscreen_canvas = matrix.CreateFrameCanvas()

#Colors
green = graphics.Color(0,150,0)
red = graphics.Color(150,0,0)
purple = graphics.Color(255,0,255)

#Button / LED setup
pressed = 0
leds = {
    18: 14,
    24: 15,
    8: 25,
    7: 19,
    9: 10
}

for button, led in leds.items():
    GPIO.setup(led, GPIO.OUT)  # led
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # button

def showReady():
    lp = 0
    # runs a simple animation with the buttons LEDS so you know it's ready.
    while lp < 5:
        for led in leds.values():
            GPIO.output(led, True)
            time.sleep(.15)
            GPIO.output(led, False)
        lp += 1

def clearlights():
    for led in leds.values():
        GPIO.output(led, False)

def lookForButtons(buttonNum):
    global pressed
    input_state = GPIO.input(buttonNum)
    if not input_state:
        clearlights()
        # print('press '+str(buttonNum))
        if buttonNum != pressed:
            # new button was pressed
            GPIO.output(leds.get(buttonNum, ''), True)
            buttontext = {
                18: 'button 1',
                8: 'button 2',
                24: 'button 3',
                7: 'button 4',
                9: 'button 5'
            }

            graphics.DrawText(offscreen_canvas, font, 5, 20, green, buttontext.get(buttonNum,''))
            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
            time.sleep(0.2)
            pressed = buttonNum

        else:
            # active button was re-pressed, turn it off and clear screen
            pressed = 0
            offscreen_canvas.Clear() 
            time.sleep(0.6)

while True:
    for key in leds:
        lookForButtons(key)
    time.sleep(.05)  # don't lock the cpu
