pi@raspberrypi:~ $ cd ~/Raspi
pi@raspberrypi:~/Raspi $ git init
Initialized empty Git repository in /home/pi/Raspi/.git/
pi@raspberrypi:~/Raspi $ pull origin master
bash: pull: command not found
pi@raspberrypi:~/Raspi $ git pull origin master
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
pi@raspberrypi:~/Raspi $ pull Raspi
bash: pull: command not found
pi@raspberrypi:~/Raspi $ git pull raspi
fatal: 'raspi' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
pi@raspberrypi:~/Raspi $ git pull Raspi
fatal: 'Raspi' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
pi@raspberrypi:~/Raspi $ git remote
pi@raspberrypi:~/Raspi $ git fetch
fatal: No remote repository specified.  Please, specify either a URL or a
remote name from which new revisions should be fetched.
pi@raspberrypi:~/Raspi $ git remote add origin git@github.com:cassidjf/Raspi.gitpi@raspberrypi:~/Raspi $ git pull
Enter passphrase for key '/home/pi/.ssh/id_rsa': 
Enter passphrase for key '/home/pi/.ssh/id_rsa': 
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 12 (delta 0), reused 9 (delta 0), pack-reused 0
Unpacking objects: 100% (12/12), done.
From github.com:cassidjf/Raspi
 * [new branch]      master     -> origin/master
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> master

pi@raspberrypi:~/Raspi $ git pull origin master
Enter passphrase for key '/home/pi/.ssh/id_rsa': 
From github.com:cassidjf/Raspi
 * branch            master     -> FETCH_HEAD
pi@raspberrypi:~/Raspi $ git add --all
pi@raspberrypi:~/Raspi $ git status -v
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   xmas leds v 1-5-19.py

diff --git a/xmas leds v 1-5-19.py b/xmas leds v 1-5-19.py
new file mode 100644
index 0000000..49dd1a2
--- /dev/null
+++ b/xmas leds v 1-5-19.py	
@@ -0,0 +1,68 @@
+import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
+from time import sleep     # Import the sleep function from the time module
+import datetime
+import time
+
+# Setup
+GPIO.setwarnings(False)    # Ignore warning for now
+GPIO.setmode(GPIO.BCM)   # Use Broadcom pin numbering not board numbering
+R2 = 21
+GPIO.setup(R2, GPIO.OUT, initial=GPIO.LOW)   # Set pin 26 to be an output pin and set initial value to low (off)
+ledOff = True
+#ledOff = False
+# Parameters
+wait=2
+tSleep=30
+tstart= datetime.time(17,00,0)
+tfinish = datetime.time(17,8,0)
+
+def nowTime():
+    now = datetime.datetime.now()
+    return now.time()
+    
+print(nowTime())
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
pi@raspberrypi:~/Raspi $ git add --all
pi@raspberrypi:~/Raspi $ git commit -am 'git setup of relay pi'
[master a0c6546] git setup of relay pi
 1 file changed, 61 insertions(+)
 create mode 100644 relay cpu setup.md
pi@raspberrypi:~/Raspi $ git push -u origin master
Enter passphrase for key '/home/pi/.ssh/id_rsa': 
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.01 KiB | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:cassidjf/Raspi.git
   680f0c0..a0c6546  master -> master
Branch master set up to track remote branch master from origin.
pi@raspberrypi:~/Raspi $ 
