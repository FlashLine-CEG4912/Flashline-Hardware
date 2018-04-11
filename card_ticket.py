from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication
#import for firebase
import time

import RPi.GPIO as GPIO
import SimpleMFRC522
import sys


#===========================FIREBASE ACCESS=======================

app = FirebaseApplication('https://flashline-d440e.firebaseio.com/', authentication=None)
authentication = FirebaseAuthentication('jOflihfoYA1KIIf5Sov98MznVYyQcyo6V47yhsel',
                                        'finrazaf@gmail.com', extra={'id': 123})
app.authentication = authentication

user = authentication.get_user()

#result = app.get('/Ticket/ticketnum', None)

reader = SimpleMFRC522.SimpleMFRC522()


while True:
    
    try:
        id, text = reader.read()

        #update printing flag
        app.put('/print',"printValue", 1 )

        #update people in line +1    
        peopleInlineVal = app.get('/Moreinfo/PeopleInLine', None)
        peopleInlineVal +=1
        #app.put('/Moreinfo',"PeopleInLine", peopleInlineVal )


        #update next available +1
        nextT = app.get('/Tickets/0/servingNumber', None)
        nextT = nextT + peopleInlineVal
        #app.put('/print',"nextAvailable", nextT )


        #update usertickets
        nowServing = app.get('/Tickets/0/servingNumber', None)
        nowServing += 1
        
        app.put('/UserTickets/tL1vNdbOe6MAGORONUaS1zQfafL2',
                'myTicket', nextT)

            
            
        
        print "updated on db"
        time.sleep(6)

    except KeyboardInterrupt:
        GPIO.cleanup()
        print "\n Terminated by User"
        sys.exit()


