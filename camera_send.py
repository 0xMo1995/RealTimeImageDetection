#!/usr/bin/env python


from picamera import PiCamera
from time import sleep, gmtime, strftime
from random import randint
import socket,select
import glob
import boto3

def take_pic():
    camera = PiCamera()
    camera.start_preview()
    for i in range(0,4):
        sleep(2)
        camera.capture('/home/pi/RealTimeImageDetection/TestImages/image%s.jpg' % i)
    camera.stop_preview()

take_pic()

count = len(glob.glob1("/home/pi/RealTimeImageDetection/TestImages",
                       "*.jpg"))

#print(count)

#data = open('','rb')
#s3.Bucket('').put_object(Key ='test.jpg',Body = data)


