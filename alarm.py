import pygame
import time
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(14, GPIO.OUT)

pygame.mixer.init()
pygame.mixer.music.load("default.mp3")


def alarm():
    
    while True:
        current_time = time.strftime("%I:%M")
        ampm = time.strftime("%p")
        input_state = GPIO.input(18)
        count = 0
        
        if current_time == "12:42" and ampm == "PM" and input_state == True and count == 0:
            if pygame.mixer.music.get_busy() == True:
                continue
            else:
                pygame.mixer.music.play()
                print(current_time , ampm)
        
        if input_state == False:
            pygame.mixer.music.stop()
            GPIO.output(14, False)
            count+=1
            break
        
        time.sleep(0.25)
