#!/usr/bin/env python

from picamera import PiCamera
from time import sleep, gmtime, strftime
from random import randint
import socket,select

def take_pic():
    camera = PiCamera()
    camera.start_preview()
    for i in range(0,4):
        sleep(2)
        camera.capture('/home/pi/RealTimeImageDetection/TestImage/image%s.jpg' % i)
    camera.stop_preview()

take_pic()

HOST = '10.189.130.117'
PORT = 137

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ('socket created')
except client.error as error:
    print('socket creation failed: %s' %(err))    
     
server_address = (HOST, PORT)
client.connect(server_address)



image = "/home/pi/RealTimeImageDetection/TestImage/image15.jpg"

file = open(image, 'rb')
image_data = file.read(2048)

while image_data:
    client.send(image_data)
    image_data = file.read(2048)

file.close()
client.close()

# print(image)
# 
# client.close()

# try:
#     print("trying to send image")
#     # open image
#     myfile = open(image, 'rb')
#     bytes = myfile.read()
#     #print(bytes)
#     size = len(bytes)
# 
#     # send image size to server
#     print size
#     sock.sendall("SIZE %s" % size)
#     answer = sock.recv(4096)
#     
#     print ('answer = %s' % answer)
# 
#     # send image to server
#     if answer == 'GOT SIZE':
#         sock.sendall(bytes)
# 
#         # check what server send
#         answer = sock.recv(4096)
#         print 'answer = %s' % answer
# 
#         if answer == 'GOT IMAGE' :
#             sock.sendall("BYE BYE ")
#             print 'Image successfully send to server'
# 
#     myfile.close()

# finally:
#      sock.close()

