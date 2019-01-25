#!/usr/bin/python
#v3 dropbox upload and file move added. location added to file name
# comment column added to data file header.
#reboot added and tested. Requires edit of .bashrc
#
#add lines at end
#sudo nano ./.bashrc
#echo running at boot
#sudo python /home/pi/Raspi/Adafruit_Python_DHT/examples/DHTv2.py
#
#committed 1/25/19

import Adafruit_DHT
from time import sleep
#import datetime
from time import sleep
from datetime import datetime
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
import os, fnmatch, shutil
from subprocess import call

path = '/home/pi/DHT_Data/'
listFiles = os.listdir(path)
pattern = "*.txt"
for entry in listFiles:
    if fnmatch.fnmatch(entry,pattern):
        print (entry)
        Upload = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + path + entry + " " + "Raspi/DHT_Data/" + entry
        call ([Upload], shell = True)
        os.rename( path + entry, path + "Archive/" + entry)
        shutil.move(path + "Archive/" + entry, path + "Archive/" + entry)



sensor = Adafruit_DHT.DHT22


pin=4
# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
#pin = 23
print()
Raspilocation = "cav_study_"
comment = "ve tested on cav_study raspi"
now = datetime.now()
fname = "/home/pi/DHT_Data/" + Raspilocation + "TH_" + now.strftime("%y_%m_%d_%H_%M_%S") + ".txt"

print(fname)

fo = open(fname,"w")
head = "TimeStamp,Temperature,Humidity," + comment + "\n"
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
