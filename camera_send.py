#!/usr/bin/env python

from picamera import PiCamera
from time import sleep, gmtime, strftime
from random import randomint
import socket,select

HOST = '127.0.0.1'
PORT = 6666

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)
camera = PiCamera()

camera.start_preview()
for i in range(0,11):
    sleep(5)
    camera.capture('/home/pi/RealTimeImageDetection/TestImage/image%s.jpg' % i)
camera.stop_preview()

# try:

    # # open image
    # myfile = open(image, 'rb')
    # bytes = myfile.read()
    # size = len(bytes)

    # # send image size to server
    # sock.sendall("SIZE %s" % size)
    # answer = sock.recv(4096)

    # print 'answer = %s' % answer

    # # send image to server
    # if answer == 'GOT SIZE':
        # sock.sendall(bytes)

        # # check what server send
        # answer = sock.recv(4096)
        # print 'answer = %s' % answer

        # if answer == 'GOT IMAGE' :
            # sock.sendall("BYE BYE ")
            # print 'Image successfully send to server'

    # myfile.close()

# finally:
    # sock.close()

