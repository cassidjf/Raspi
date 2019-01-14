+now = datetime.datetime.now()
+print(now)
+
+print(now.date(),time.time(),nowTime)
+
+while True: # Run forever
+    now = nowTime()
+    print(now)
+    if now < tstart:
+        if not(ledOff):
+            GPIO.output(R2, GPIO.LOW) # Turn off
+            print ('turn led off')
+            ledOff = True
+        else:
+            print('within time window and led is off')
+            
+    if now > tstart:
+        if now < tfinish:
+            print('within time window')
+            if ledOff:
+                GPIO.output(R2, GPIO.HIGH) # Turn on
+                print('led turned on')
+                ledOff = False
+            
+            else:
+                print(' led is on during window')
+                
+        if now > tfinish:
+            print('beyond time window')
+            if not(ledOff) :
+                print(' beyond window turn led off')
+                ledOff = True
+                GPIO.output(R2, GPIO.LOW) # Turn off
+                
+            else:
+                print('beyond window led was off')
+            
+    
+    sleep(tSleep)
+    print("end of loop")
+    
+# GPIO.output(R2, GPIO.HIGH) # Turn on
+# sleep(wait) # Sleep for wait seconds
+# GPIO.output(R2, GPIO.LOW) # Turn off
+# sleep(wait) # Sleep for wait seconds
pi@raspberrypi:~/Raspi $ git commit -am 'First upload from felay pi'
[master 680f0c0] First upload from felay pi
 1 file changed, 68 insertions(+)
 create mode 100644 xmas leds v 1-5-19.py
pi@raspberrypi:~/Raspi $ git push -u origin master
Enter passphrase for key '/home/pi/.ssh/id_rsa': 
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 931 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:cassidjf/Raspi.git
   827f4c7..680f0c0  master -> master
Branch master set up to track remote branch master from origin.
pi@raspberrypi:~/Raspi $ 
