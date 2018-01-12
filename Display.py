#!/usr/bin/python

# This is assuming you've followed the instructions at
# https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices

# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

# This project was created by Bob Clagett of I Like To Make Stuff
# More details and build video available at http://www.iliketomakestuff.com/

import Image
import ImageDraw
import time
import os
from rgbmatrix import Adafruit_RGBmatrix

import RPi.GPIO as GPIO

imagePath = '/home/pi/rpi-rgb-led-matrix-master/'
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)
matrix.SetWriteCycles(4)
# Bitmap example w/graphics prims
image = Image.new("1", (64, 32))  # Can be larger than matrix if wanted!!


def showReady():
    image = Image.open(imagePath + "logo.jpg")
    image.load()
    matrix.SetImage(image.im.id, 0, 1)
    time.sleep(2)
    matrix.Clear()

# setup complete, start running stuff
matrix.Clear()
print('PiSign loaded.....  rock on    \m/')
showReady()
