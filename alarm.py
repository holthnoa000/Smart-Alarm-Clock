import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load("default.mp3")


def alarm():
    current_time = time.strftime("%I:%M")
    ampm = time.strftime("%p")
    
    if current_time == "11:37" and ampm == "AM":
        pygame.mixer.music.play()
        print(current_time , ampm)
        while pygame.mixer.music.get_busy() == True:
            continue
    
while True:
    alarm()
    time.sleep(1)
