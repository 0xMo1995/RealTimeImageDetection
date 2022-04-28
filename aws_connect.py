from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import requests
import time
import json
import camera_send

def helloworld(self,params,packet):
	print('received message from AWS IoT Core')
	print('topic: ' + packet.topic)
	print('Payload: ', str(packet.payload.decode("utf-8")))
	msg_in = json.loads(str(packet.payload.decode("utf-8")))
	if str(msg_in['message']) == "take pic":
		print("Taking Pics")
		camera_send.take_pic()
		print('Image sent to S3')
		camera_send.send_pic()
		

myMQTTClient = AWSIoTMQTTClient("TestClientID") 
myMQTTClient.configureEndpoint("a3oc4ncpl2l21b-ats.iot.us-east-1.amazonaws.com", 8883)

myMQTTClient.configureCredentials("/home/pi/RealTimeImageDetection/AmazonRootCA1.pem", "/home/pi/RealTimeImageDetection/private.pem.key", "/home/pi/RealTimeImageDetection/certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print ('Initiating IoT core topic ...')
myMQTTClient.connect()

myMQTTClient.subscribe("RTOS/sub",1,helloworld)

while True:
	time.sleep(5)

# print("Publishing Message from RPI")
# myMQTTClient.publish(
	# topic = "home/helloworld",
	# QoS = 1,
	# payload = "{'Message':'Message by RPI'}"
	# )
