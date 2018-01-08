import socket,json,time
import serial
from PIL import Image

######setup
neuroSocket = socket.create_connection(("127.0.0.1",13854))
data = '{"appName":"appName","appKey":"appKey"}'
formatt = '{"enableRawOutput":true,"format":"Json"}'
#print data
#print formatt

#r = neuroSocket.send(data)
#print r
r = neuroSocket.sendall(formatt)
ser = serial.Serial("COM6", 9600)
while ser.read() != '1':
        ser.read()
        print "arduino setup"

print r
print "Connecting...",r,"connected"
#image = Image.open('stop.jpg')
timeDiff=0
start=time.time()
blinkc=0
blink_flag=0
counter=0
fwd="2"
while True:
    rep = neuroSocket.recv(1024)
    if("blink" in rep):
        print "blink"
        print rep
        blinkc=blinkc+1
    timeDiff=time.time()- start
    if timeDiff>3:
        #image.close()
        print blinkc
        if ((blink_flag==0 and blinkc==0) or blinkc>4) :
            image = Image.open('stop.jpg')
            image.show()
            fwd="2"
            ser.write(fwd.encode())
            print "stop"
            image.close()
            if blinkc >3 :
                    blink_flag=0
        elif blink_flag==1 and blinkc==0 :
            image = Image.open('moving.jpg')
            image.show()
            print "move"
            blink_flag=1
            fwd="1"
            ser.write(fwd.encode())
            image.close()
        else:
            if(counter%3==0):
                image = Image.open('left.jpg')
                image.show()
                print "left"
                blink_flag=1
                image.close()
            elif(counter%3==1):
                image = Image.open('forward.jpg')
                image.show()
                print "forward"
                blink_flag=1
                image.close()
            else:
                image = Image.open('right.jpg')
                image.show()
                print "right"
                blink_flag=1
                image.close()
            counter=counter+1;

        timeDiff=0
        start=time.time()
        blinkc=0
    #if("attention" in rep):
     #   print "waves"
      #  rep = rep.split('\r')
        #print rep
       # print "\n"
        #for data in rep:
         #   print data
            #parsed_data=json.loads(data)            #parsed_data is dict
            #print parsed_data
            #print "poor",parsed_data['poorSignal']
            #print "attention",parsed_data['eSense'][0]['attention']
    #time.sleep(2)

    

'''
while True:
    rep = neuroSocket.recv(1024)
    #rep = rep.split('\r')
    jsonData = json.loads(rep)
    for e in jsonData:
        for k,v in e.items():
            if k!='rawEeg':
                print k,v
    #for key,value in jsonData.items():
     #   print key," : ",value
   # print rep

timeDiff=0
flag=1
while True:
    blinkc=0
    start=time.time()
    while timeDiff<1:
        rep = neuroSocket.recv(1024)
        if("blink" in rep):
            print "p"
            blinkc=blinkc+1
        timeDiff=time.time()- start
        #print timeDiff
    timeDiff=0
    print "blink :", blinkc
    #flag=int(raw_input())
   


        if("blink" in rep):
             print "blink2"
        else:
            print "blink1"
        time.sleep(1)
        print rep
        #time.sleep()
    #if("poor" in rep):
    #        print "Waves"
    #        print rep
    #print "START"
    #print rep.split('\r')
    #print "END"
'''
