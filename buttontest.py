import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Button / LED setup
pressed = 0
leds = {
    18: 14,
    24: 15,
    8: 25,
    7: 19
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
            time.sleep(0.2)
            pressed = buttonNum

        else:
            # active button was re-pressed, turn it off and clear screen
            pressed = 0
            time.sleep(0.6)
            
while True:
    for key in leds:
        lookForButtons(key)
    time.sleep(.05)  # don't lock the cpu
