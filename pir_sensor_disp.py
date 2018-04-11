import sys
import time
import RPi.GPIO as gpio
import os, subprocess, time
os.environ['DISPLAY'] = ":0"

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(40,gpio.IN)

counter=0

def motion_detect():
    global counter
    
    try:
        while True:
            time.sleep(1)
            if gpio.input(40)==1:
                print "Motion Detected"
                subprocess.call('xset dpms force on', shell=True)
                counter = 0
#		time.sleep(0.2)
	    else:
                counter +=1
                print "No motion detected"
                
                if (counter == 10):
                    subprocess.call('xset dpms force off', shell=True)
                

    except KeyboardInterrupt:
        gpio.cleanup()
        print "\n Terminated by User"
        sys.exit()


if __name__ == "__main__":
    motion_detect()
