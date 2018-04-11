from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication
#import for firebase
import time
import tk_firebase

#===========================FIREBASE ACCESS=======================

app = FirebaseApplication('https://adminflashline.firebaseio.com/', authentication=None)
authentication = FirebaseAuthentication('pt14BYHQUUxMhFoa0Eigtr59aIa3Gyfvwoc209Tu',
                                        'finrazaf@gmail.com', extra={'id': 123})
app.authentication = authentication

user = authentication.get_user()

result = app.get('/Ticket/ticketnum', None)
print ('===============================')
print('Result: ' + str(result))

instance = tk_firebase.tk_firebase()

while True:
    time.sleep(8)
    #instance.ma()
    instance.updateDB()

    
