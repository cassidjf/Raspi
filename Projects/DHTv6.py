#DHTv6 2-14-19

from datetime import datetime
import numpy as np
from time import sleep
""" ================== Animated line plot ================== """
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Adafruit_DHT
#import datetime
from time import sleep
from datetime import datetime

from matplotlib.dates import DateFormatter
from matplotlib import dates
import matplotlib.dates as mdates
import matplotlib
from matplotlib.pyplot import figure


def readSensor():
    sensor = Adafruit_DHT.DHT22
    pin=4
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    tempf = 32 + 9 * temperature /5
    return round(tempf,1),round(humidity,1)

def st(temp,hum,ns): 
    #use float array
    nr=1
    print ('st,s')
    print(temp,hum)
    if len(temp) > ns - 1:
        stemp = np.array(temp)
        shum = np.array(hum)
        print('ss')
        print(shum)
        datat = stemp[-ns:]
        datah = shum[-ns:]
        print('data')
        print(len(datat))
        print(datat)
        avg = str(round(np.mean(datat),nr)) + ' | ' + str(round(np.mean(datah),nr))
        print (avg)
        min = str(round(np.min(datat),nr)) + ' | ' + str(round(np.min(datah),nr))
        print(min)
        max = str(round(np.max(datat),nr)) + ' | ' + str(round(np.max(datah),nr))
        print(max)
        range = str(round(np.ptp(datat),nr)) + ' | ' + str(round(np.ptp(datah),nr))
        print(range)
        sd = str(round(np.std(datat),nr)) + ' | ' + str(round(np.std(datah),nr))
        print(sd)
        return [avg, min ,max, sd]
    else:
        return[0.0,0.0,0.0,0.0]


'''sensor = Adafruit_DHT.DHT22
pin=4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
tempf = 32 + 9 * temperature /5
print(i)
print(humidity)
print(tempf)'''

nsample=4000

Raspilocation = "cav_study_"
comment = "  tested on cav_study raspi"
now = datetime.now()
nowstr = now.strftime("%y_%m_%d_%H_%M_%S") 
Raspilocation = "cav_study_"
comment = "  tested on cav_study raspi"



fname = "/home/pi/DHT_Data/" + Raspilocation + "TH_" + nowstr + ".txt"
# Create data file
fo = open(fname,"w")
head = "TimeStamp,Temperature,Humidity,Time" + fname + comment + "\n"
fo.write(head)
fo.close()




plt.close('all')

# Define the axes 
left, width = 0.075, .9
bottom, height = 0.1, .3
#bottom_h = left_h = left+width+0.02
rect_txt =[left, bottom + .7, width, height-.15] 
rect_hum = [left, bottom + .35, width, height] 
rect_temp = [left, bottom , width, height ]
#plt.close('all')

fig = plt.figure(figsize=(12,6))



temp = plt.axes(rect_temp) 
hum = plt.axes(rect_hum)
txt = plt.axes(rect_txt)
hum.set_ylabel('Humidity (% RH)')
temp.set_ylabel('Temperature (*F)')
temp.grid(True)
hum.grid(True)
temp.set_xlabel('Time (minutes)')
'''
# Rotate date labels automatically
fig.autofmt_xdate()

myFmt = DateFormatter("%b %d %H:%M")
temp.xaxis.set_major_formatter(myFmt)
'''
#temp.set_xlim(0,100)
#temp.set_ylim(0,100)
txt.set_xlim(0,1)
txt.set_ylim(0,1)
txt.axes.get_xaxis().set_visible(False)
txt.axes.get_yaxis().set_visible(False)


#Define text blocks
cr = '\n'
l11 = 'Initial data at 19/01/19 08:23:01'
l21 = 'Last data at 19/01/31 16:12:33'
l31= 'Current datetime is 19/01/31 20:48:32'
npoints = 'Number of points is 121'


b1 = l31 + cr + l21 + cr + l11 + cr + npoints  

#peg upper corner  

txt.text(.01,.1,b1)  

l21 = 'Temperature: 74.9*F'  
l22 = 'Humidity: 34.2%'
b2= l21 + cr + l22
txt.text(.55,.15,b2, size =20)


#Define plot lines

ptime=[]
ptemp=[]
phum=[]

p1, = temp.plot(ptime,ptemp)
p2, = hum.plot(ptime,phum,color='r')
p3, = txt.plot([],[])
pp =[p1, p2, p3]



def animate(i,*args):
    print ('****',fname,nowstr)
    now = datetime.now()
    print(now)
    print(i,i*i)
    #fig = plt.figure()
    #fig.clear()
    
    #fig = plt.figure()
    #plt.clf()
    #fig, ax = plt.subplots()
    
    tempf,humidity = readSensor()
    print(i)
    print(humidity)
    print(tempf)
    timeStamp = datetime.today()
    print(timeStamp)
    # write to data file
    fo = open(fname,"a")
    
    dd = '{0:0.1f},{1:0.1f}'.format(tempf, humidity)
    ts = now.strftime("%m/%d/%y %H:%M:%S")
    t1 =now.strftime("%m/%d/%y %H:%M:%S")
    print('t1 = ',t1)
    tss= datetime.strptime(t1, '%m/%d/%y %H:%M:%S')
    print('tss = ',tss)
    #ttt= dates.date2num(line[0])
    ttt= dates.date2num(tss)
    print('ttt ',ttt)   
    data1 = ts + "," + dd + ',' + str(ttt) + '\n'
    
    fo.write(data1)
    print(data1)
        #dt = datetime.today()
        #ttt = dt.timestamp()
        #ttt = int(now.strftime("%m/%d/%y %H:%M"))
        #print('ptime old ',ptime)
    ptime.append(ttt)
        
    
    ptemp.append(tempf)
    phum.append(humidity)
    
    # calculate stats
    # Initialize lists 



    ns=12
    
    ss = st(ptemp,phum,ns) 
    print(ss)
    

    aa=[[],[],[]]
    aa[1]=ss
    ns=144
    
    ss = st(ptemp,phum,ns)

    aa[2]=ss 

    ns = len(ptemp)
    
    ss = st(ptemp,phum,ns)


    aa[0] = ss
    print('aa0,aa')
    print(aa)
    #exit()

    col_labels = ['avg', 'min', 'max','std'] 
    row_labels = ['All Data', 'Last Hour', 'Last 12 Hrs']
    table_vals = aa#[[d, ss[1], ss[2], ss[4]], [21, 22, 23,22], [31, 32, 33,34]]

    
    
    
    ############
    #############
    
    
    
    
    #t1.set_text(str(i) + ' ' + str(i*i))
    
    #print(y)
    #line[0].set_data(ptime,ptemp)
    #line[1].set_data(ptime,phum)
    #ax.set_data(x,x)
    #ax1.clear()
    #ax1.plot(ptime,ptemp)
    #ax2.clear()
    #ax2.plot(ptime,phum)
    '''yy = i+5
    hum.set_xlim(0,50)
    hum.set_ylim(0,yy)'''
    temp.lines=[]
    hum.lines = []
    txt.clear()
    #t1 = txt.text(0.5,0.5,str(i))
    cr = '\n'
    l11 = 'Initial data at ' + nowstr
    
    t1 =now.strftime("%m/%d/%y %H:%M:%S")
    print(t1)
    l21 = 'Last data at ' + t1
    l31= 'Current datetime is ' + t1
    npoints = 'Number of points is ' + str(i)


    b1 = l21 + cr + l11 + cr + npoints  

    #peg upper corner  

    txt.text(.01,.1,b1)  

    l21 = 'Temperature: ' + str(round(tempf,1)) + '*F'  
    l22 = 'Humidity: ' + str(round(humidity,1))+ '%'
    b2= l21 + cr + l22
    txt.text(.25,.15,b2, size =20)
    
    the_table = txt.table(cellText=table_vals, 
     colWidths=[.06] * 4,
     rowLabels=row_labels,
     colLabels=col_labels,
     loc='lower right',bbox=[.63,.1,.33,.8])
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)

    
    
    
    '''hum.set_ylabel('Humidity (% RH)')
    temp.set_ylabel('Temperature (*F)')
    temp.grid(True)
    hum.grid(True)
    hum.set_xticklabels([]
    hum.set_xlabel('Time (minutes)')'''
    temp.plot(ptime,ptemp,color='b')
    
    fmt = mdates.DateFormatter('%b %d %H:%M')
    temp.xaxis.set_major_formatter(fmt)
    
    fig.autofmt_xdate(rotation = 45)
    plt.xticks(rotation=45)
    
    #fig.autofmt_xdata()
    #temp.fmt_xdata = mdates.DateFormatter('%H:%M:%S')
    
    
    #pp[0].set_data(ptime,ptemp)
    hum.plot(ptime,phum,color='r')
    hum.set_xticklabels([])
    
    
    #hum.xaxis_date()
        
    return pp


args =(fname,nowstr)
print(args)
print(' call ani')
ani = animation.FuncAnimation( fig, animate, fargs =(fname,nowstr,),interval=300000, blit=False)
plt.show()












