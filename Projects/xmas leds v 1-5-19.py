import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
import datetime
import time

# Setup
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)   # Use Broadcom pin numbering not board numbering
R2 = 21
GPIO.setup(R2, GPIO.OUT, initial=GPIO.LOW)   # Set pin 26 to be an output pin and set initial value to low (off)
ledOff = True
#ledOff = False
# Parameters
wait=2
tSleep=30
tstart= datetime.time(17,00,0)
tfinish = datetime.time(17,8,0)

def nowTime():
    now = datetime.datetime.now()
    return now.time()
    
print(nowTime())
now = datetime.datetime.now()
print(now)

print(now.date(),time.time(),nowTime)

while True: # Run forever
    now = nowTime()
    print(now)
    if now < tstart:
        if not(ledOff):
            GPIO.output(R2, GPIO.LOW) # Turn off
            print ('turn led off')
            ledOff = True
        else:
            print('within time window and led is off')
            
    if now > tstart:
        if now < tfinish:
            print('within time window')
            if ledOff:
                GPIO.output(R2, GPIO.HIGH) # Turn on
                print('led turned on')
                ledOff = False
            
            else:
                print(' led is on during window')
                
        if now > tfinish:
            print('beyond time window')
            if not(ledOff) :
                print(' beyond window turn led off')
                ledOff = True
                GPIO.output(R2, GPIO.LOW) # Turn off
                
            else:
                print('beyond window led was off')
            
    
    sleep(tSleep)
    print("end of loop")
    
# GPIO.output(R2, GPIO.HIGH) # Turn on
# sleep(wait) # Sleep for wait seconds
# GPIO.output(R2, GPIO.LOW) # Turn off
# sleep(wait) # Sleep for wait seconds
