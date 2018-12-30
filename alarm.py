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
    count = 0
    
    while True:
        current_time = time.strftime("%I:%M")
        ampm = time.strftime("%p")
        input_state = GPIO.input(18)
        #print (count)
        
        if current_time == "12:24" and ampm == "PM" and input_state == True and count == 0:
            if pygame.mixer.music.get_busy() == True:
                continue
            else:
                pygame.mixer.music.play()
                print(current_time , ampm)
                GPIO.output(14, True)
        
        if input_state == False: #snooze button
            pygame.mixer.music.stop()
            GPIO.output(14, False)
            count+=1
            
        elif count >= 1: #if the button has been pressed, pause the program for one minute and then reset the button state back to 0.
            time.sleep(60)
            count = 0
        
        time.sleep(0.2)
        
    
alarm() 
