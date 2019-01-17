#!/usr/bin/python


import Adafruit_DHT
from time import sleep
#import datetime
from time import sleep
from datetime import datetime
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT22


pin=4
# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
#pin = 23
print()
now = datetime.now()
fname = "TH_" + now.strftime("%y_%m_%d_%H_%M_%S") + ".txt"

print(fname)

fo = open(fname,"w")
head = "TimeStamp,Temperature,Humidity\n"
fo.write(head)
fo.close()

while True :
# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
    if humidity is not None and temperature is not None:
        now = datetime.now()
        print(now)
        fo = open(fname,"a")
        tempf = 32 + 9 * temperature /5
        dd = '{0:0.1f},{1:0.1f}'.format(tempf, humidity)
        data = now.strftime("%m/%d/%y %H:%M") + "," + dd
        data1 = data + "\n"
        fo.write(data1)
        print(data)
        
        
        
        print(dd)
        print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(tempf, humidity))
        print()
        fo.close()
        sleep(300)
        

    



    else:
        print('Failed to get reading. Try again!')
