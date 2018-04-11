#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time

#import for the server
import requests
#read from server
r = requests.get('https://apfflashline.herokuapp.com/institutions/5a1ad023873e2b14c0f2d172/buildings/5a1ad023873e2b14c0f2d17b')
data_req = r.json()
print('')
print ("Using python requests library: ")
print('')
print ("Number being served: 10 " )
print ("Next ticket available " + str(data_req['actualNumber']))
print('')
reader = SimpleMFRC522.SimpleMFRC522()

try:
#	text = raw_input('Enter the data:')
        print("Place your tag to pick a ticket")
	id, text = reader.read()
	r_2 = requests.post('https://apfflashline.herokuapp.com/institutions/5a1ad023873e2b14c0f2d172/buildings/5a1ad023873e2b14c0f2d17b', json={"actualNumber": "5"})
        data_postreq = r_2.json()
        print ("Ticket picked ")
        time.sleep(1)
        print ("Number being served: 10 " )
        print ("Next ticket available " + str(data_postreq))

        time.sleep(1)
        print("-------------------------------------------------")
	print('This is the ID of the data: ', id)
	print('This is the data in the card: ', text)
        print("-------------------------------------------------")
        time.sleep(3)
	
	print ("Now place your tag to write the ticket number")
	reader.write(str(data_postreq))
	print("Written")
	time.sleep(3)
	
	print("Place your tag to check the data in the card")
	id1, text1 = reader.read()
	print("-------------------------------------------------")
	print('This is the ID of the data: ', id1)
	print('This is the data in the card: ', text1)
        print("-------------------------------------------------")
        
finally:
	GPIO.cleanup()

