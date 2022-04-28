#!/usr/bin/env python


from picamera import PiCamera
from time import sleep, gmtime, strftime
from random import randint
import socket,select
import glob
import boto3

s3 = boto3.resource('s3')
def take_pic():
    camera = PiCamera()
    camera.start_preview()
    
    count = len(glob.glob1("/home/pi/RealTimeImageDetection/TestImages",
                       "*.jpg"))
    
    for i in range(count,count + 4):
        sleep(2)
        camera.capture('/home/pi/RealTimeImageDetection/TestImages/image%s.jpg' % i)
    camera.stop_preview()
    
def send_pic():
    count = len(glob.glob1("/home/pi/RealTimeImageDetection/TestImages",
                       "*.jpg"))
    for i in range(count-4,count):
        data = open('/home/pi/RealTimeImageDetection/TestImages/image%s.jpg' %i,'rb')
        s3.Bucket('raspi-images-class').put_object(Key='test%s.jpg'%i,Body = data)

#take_pic()
#send_pic()



#print(count)

#data = open('','rb')
#s3.Bucket('').put_object(Key ='test.jpg',Body = data)


