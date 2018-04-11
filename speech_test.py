from subprocess import call
import time
#import pyttsx
time.sleep(2)


#os.system("say 'hello'")
speech ="Now serving, ticket number 12"
call(["espeak","-ven+f2", speech])



 
##text_to_speech = talkey.Talkey()
## 
##text_to_speech.say("Now serving, Professor Dan, ticket number 123456788")
##
