from Tkinter import *
#Tkinter with a capital "T" is for python 2

from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication
#import for firebase
from firebase_streaming import Firebase

import time

from subprocess import call



#class tk_firebase:

##fb = Firebase('https://adminflashline.firebaseio.com/Ticket/')
##childos = fb.child("ticketnum")
##print childos

#===========================FIREBASE ACCESS=======================

app = FirebaseApplication('https://flashline-d440e.firebaseio.com/', authentication=None)
authentication = FirebaseAuthentication('jOflihfoYA1KIIf5Sov98MznVYyQcyo6V47yhsel',
                                        'finrazaf@gmail.com', extra={'id': 123})
app.authentication = authentication

user = authentication.get_user()

result = app.get('/Tickets/0/servingNumber', None)
print ('===============================')
print('Result: ' + str(result))




#===========================UI TKINTER=======================
#global variables for methods
buttoncolor = "blue"
cardTaped = False
getValue = 0
oldValue =0

#Global variables for UI
nowServing = app.get('/Tickets/0/servingNumber', None)
nWaiting = app.get('/Moreinfo/PeopleInLine', None)
nextAvailable = 10
nbservedStr = "Now Serving"

institutionStr = "Institution name"
waitingStr = "Waiting on the line: " + str(nWaiting)
nextavailableStr = "Next available number: " + str(nextAvailable)


#Methods
def pickATicket():

    global buttoncolor

    #increment the num of waiting
    global nWaiting
    nWaiting += 1
    global waitingStr
    waitingStr = "Waiting on the line: " + str(nWaiting)
    nbwaiting ["text"] = waitingStr

##    
##    if buttoncolor == 'blue':
##        nbservedNUM["bg"] = "red"
##        buttoncolor = "red"
##        
##
##    else:
##        
##        nbservedNUM["bg"] = "blue"
##        buttoncolor = "blue"
##    bottomlabel1 ["text"] = "Please tap you card"

    #update now serving in database
    global nowServing
    nowServing += 1
    app.put('/Ticket',"ticketnum", nowServing )
    nbservedNUM["text"] = app.get('/Ticket/ticketnum', None)
    
def updateDB():
    global getValue
    global oldValue
    global app
    global nbservedNum
    global institutionStr
    global nWaiting
    global waitingStr
    global nextAvailable
    global nbnextavailableStr
    
    while True:
        

        #update institution name
        instit = app.get('/Institutions/0/name', None)
        subinstit = app.get('/Institutions/0/subinstitutions/0/name', None)
        thelabel["text"] = instit + ": " + subinstit

        #update now serving
        time.sleep(2)
        getValue = app.get('/Tickets/0/servingNumber', None)
        
        
        print "---"
        print getValue
        nbservedNUM["text"] = getValue
        root.update_idletasks()

        
        #if (oldValue != getValue):
            #speech ="Now serving, ticket number " + str(getValue)
            #call(["espeak","-ven+f2", speech])

        oldValue = app.get('/Tickets/0/servingNumber', None)


        #update printing
        printingFlag = app.get('/print/printValue', None)
        if (printingFlag == 1):
            
            bottomlabel1["text"] = "Printing your ticket..."
            root.update_idletasks()
            time.sleep(5)
            app.put('/print',"printValue", 0 )
            bottomlabel1["text"] = "Please tap your card"
            root.update_idletasks()
        
        #update people in line
        nWaiting = app.get('/Moreinfo/PeopleInLine', None)
        waitingStr = "Waiting on the line: " + str(nWaiting)
        nbwaiting["text"] = waitingStr
        
        
        #update next available
        nextAvailable = app.get('/Institutions/0/subinstitutions/0/waitingTime', None)
        nbnextavailableStr = "Average waiting time: " + str(nextAvailable)
        nbnextavailable["text"] = nbnextavailableStr
        
        root.update_idletasks()
     #nbservedNUM["text"] = app.get('/Ticket/ticketnum', None)
     #print "R4"


#UI
root = Tk()
root.title("Ticket system")
root.minsize(width=800, height=400)
root.configure(bg="white")

#frames 
topframe = Frame(root,bg="white")
topframe.pack(side=TOP)

middleframe = Frame(root,bg="#BBDEFB")
middleframe.pack(side=TOP)

bottomframe2= Frame(root,bg="green")
bottomframe2.pack(side=BOTTOM)
bottomlabel2 = Label(bottomframe2, bg="white", height=4,text="-")
bottomlabel2.pack()

bottomframe1= Frame(root,bg="green")
bottomframe1.pack(side=BOTTOM)
bottomlabel1 = Label(bottomframe1,font=("Helvetica",14,"bold"),fg="red",
                     bg="white", height=4, text="Please tap your card")

bottomlabel1.pack()

bottomframeB= Frame(root,bg="white", pady=15)
bottomframeB.pack(side=BOTTOM)


#labels
thelabel = Label(topframe,bg="white",height=3,
                 font=("Helvetica",14,"bold"),text="INSTITUTION NAME")


nbwaiting = Label(topframe,bg="white",height=3, width=30,
                  font=("Helvetica",13,"bold"), text=waitingStr)


nbnextavailable = Label(topframe,bg="white",height=3, width=30,
                        font=("Helvetica",13,"bold"),text=nextavailableStr)

#main label

nbserved = Label(middleframe,bg="#BBDEFB",height=2, width=10 ,
                font=("Helvetica",15,"bold"),text=nbservedStr)
nbservedNUM = Label(middleframe, bg="#BBDEFB",height=2, width=5,
                font=("Helvetica",50,"bold"),text=nowServing)


#button
#button1 = Button(bottomframeB, command=pickATicket, bg= '#448AFF',
#                 activebackground='#448AFF', text="Pick a ticket", fg="white")



#pack() for labels and buttons
#button1.pack()

thelabel.pack()


nbwaiting.pack(side=LEFT)

nbnextavailable.pack(side=LEFT)

nbserved.pack()
nbservedNUM.pack()



print "R1"
root.after(2000, updateDB)
print "R2"

root.mainloop()


