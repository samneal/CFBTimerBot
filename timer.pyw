import ImageGrab, Image, ImageOps
from hue import Hue
import os
import datetime
import requests, json, os, sys
import time
from numpy import *

coordinate = (950,350) ##Find a pixel with a continuous color, and find its coordinates in Photoshop
colorVal = 75 ##Set colorVal to match pixel color value


def screenGrab():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) + '.png', 'PNG')
    im = ImageOps.grayscale(ImageGrab.grab(box))
    return im

def grab():
    box = ()
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a

def checkHealth():
    ##Uncomment two lines below, and run to find the baseline color value to set to colorVal up top. This will be the continuous non-commercial pixel color
    ##print "Color value at pixel to set to ColorVal "
    ##print screenGrab().getpixel(coordinate)
    it = 0
    iterator = 0
    firstTime = 0
    commercialStart = 0
    commercialStop = 0
    tempCommercialTime = 0
    totalCommercialTime = 0
    while True:
        time.sleep(1) ##how often the program checks for pixel color changes
        s = screenGrab()
        if (s.getpixel(coordinate) != colorVal): ##checks whether pixel is out of defined range
            commercialStart = time.time()
            while screenGrab().getpixel(coordinate) != colorVal:
                time.sleep(1)
            commercialStop = time.time()
            tempCommercialTime = commercialStop - commercialStart

        else:
            totalCommercialTime += tempCommercialTime
            commericalStart = 0
            commercialStop = 0
            tempCommercialTime = 0
            iterator += 1
            if iterator%15 == 0:
                ##Prints commercial time every 15 seconds
                print "Total commerical time in seconds: "
                print totalCommercialTime
        ##This deletes the png files
        dir_name = "/Code/"   ##put the directory name here
        test = os.listdir(dir_name)
        it = it + 1
        if it%10 == 0:
            for item in test:
                if item.endswith(".png"):
                    os.remove(os.path.join(dir_name, item))
    
def main():
    checkHealth()

if __name__ == '__main__':
    main()
