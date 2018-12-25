import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(14, GPIO.OUT)


while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        GPIO.output(14, True)
    else:
        GPIO.output(14, False)
    time.sleep(0.2)
    
