import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
import random

class device:
    MAC=0
    destMAC=0
    content=""
    def set_values(self,source,dest,data):
        self.MAC=source
        self.destMAC=dest
        self.content=data

class HUB:
    Source=0
    Dest=0
    Data=""
    def hub_values(self,source,dest,data):
        self.Source=source
        self.Dest=dest
        self.Data=data

class SWITCH:
    MAC_LIST=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]


switch=SWITCH()
hub1=HUB()
hub2=HUB()

####################### MAIN  ###########
D=[]
n=10
print("__________________________________________________________________")
print("              DATA-LINK LAYER IMPLEMENTATION ")

print("__________________________________________________________________")

for i in range(n):
    D.append(device())
print("-----------------------------------------------------------------")
print("10 Devices created")
print("-----------------------------------------------------------------")
print("Setting MAC address for each device")
m=0
while m<4:
    print(".")
    m+=1
    time.sleep(0.4)
print("-----------------------------------------------------------------")
for i in range(n):
    D[i].MAC=i
    print("MAC address for device", i ,"-> ",i)
print("-----------------------------------------------------------------")
print("Starting service.......")
m=0
while m<4:
    print(".")
    m += 1
    time.sleep(0.4)
print("-----------------------------------------------------------------")
source=int(input("Enter Source MAC:"))
destination=int(input("Enter Destination MAC:"))
data=input("Enter Data:")
print("-----------------------------------------------------------------")
print("Source device setting up......")
m=0
while m<4:
    print(".")
    m += 1
    time.sleep(0.4)

for i in range(n):
    if i==source:
        D[i].set_values(source,destination,data)
        #print(D[i].MAC)
        #print(D[i].destMAC)
        #print(D[i].content)
print("Source device initialized successfully")
print("-----------------------------------------------------------------")

######################## hub1 ##########################
if source <=4 and destination <=4:
    print("Connecting to HUB-1 .......")
    m=0
    while m<4:
        print(".")
        m += 1
        time.sleep(0.4)

    hub1.hub_values(D[source].MAC,D[source].destMAC,D[source].content)
    print("HUB-1 recieved information successfully from Device :",source)
    print("Source MAC      =",hub1.Source)
    print("Destination MAC =",hub1.Dest)
    print("Message         =",hub1.Data)
    print("-----------------------------------------------------------------")
    print("HUB-1 is broadcasting the message.....")
    m=0
    while m<4:
        print(".")
        m += 1
        time.sleep(0.4)
        print("_________________________________________________________________")

    for i in range(int(n/2)):
        if i!=source:
            if D[i].MAC==hub1.Dest:
                print("Device", i, "ACCEPTED the request.")
                print("Framing....")
                while m < 4:
                    print(".")
                    m += 1
                    time.sleep(0.4)
                while len(data) % 4 != 0:
                    data = '0' + data

                print("Message will be divided into", int(len(data) / 4), "frames....")
                print("Frames are sending to reciever using STOP & WAIT protocol......")

                for i in range(int(len(data) / 4)):
                    frame = data[i * 4:(i + 1) * 4]
                    values = range(10, 30)
                    Time = random.choice(values) / 100
                    time.sleep(Time)  # wait for random amount of time
                    # print(frame)
                    D[destination].content = D[destination].content + frame
                    print("--------------------------------")
                    print("Frame", i, "sent!!")
                    time.sleep(Time)  # wait for random amount of time
                    print("ACK", i + 1, "recieved!!")
                    print("Round Trip time = ", 2 * Time, "ms")
                    print("---------------------------------")
                    if i + 1 != int(len(data) / 4):
                        print("Frame", i + 1, "to be sent!!")
                    if i == int(len(data) / 4) - 1:
                        print(int(len(data) / 4), "frames are successfully transmitted!!!")

            else:
                print("Device",i,"discarded request!")
    print("_________________________________________________________________")
    print("Data recieved by device",destination,":",D[source].content)
    print("_________________________________________________________________")
    print("-----------------------------------------------------------------")

####################   hub2 ####################################

if source >4 and destination >4:
    print("Connecting to HUB-2 .......")
    m=0
    while m<4:
        print(".")
        m += 1
        time.sleep(0.4)

    hub2.hub_values(D[source].MAC,D[source].destMAC,D[source].content)
    print("HUB-2 recieved information successfully from Device :",source)
    print("Source MAC      =",hub1.Source)
    print("Destination MAC =",hub1.Dest)
    print("Message         =",hub1.Data)
    print("-----------------------------------------------------------------")
    print("HUB-2 is broadcasting the message.....")
    m=0
    while m<4:
        print(".")
        m += 1
        time.sleep(0.4)
        print("_________________________________________________________________")

    for i in range(int(n/2),n):
        if i!=source:
            if D[i].MAC==hub2.Dest:
                print("Device", i, "ACCEPTED request.")
                print("Framing....")
                while m < 4:
                    print(".")
                    m += 1
                    time.sleep(0.4)
                while len(data) % 4 != 0:
                    data = '0' + data

                print("Message will be divided into", int(len(data) / 4), "frames....")
                print("Frames are sending to reciever using STOP & WAIT protocol......")

                for i in range(int(len(data) / 4)):
                    frame = data[i * 4:(i + 1) * 4]
                    values = range(10, 30)
                    Time = random.choice(values) / 100
                    time.sleep(Time)  # wait for random amount of time
                    # print(frame)
                    D[destination].content = D[destination].content + frame
                    print("--------------------------------")
                    print("Frame", i, "sent!!")
                    time.sleep(Time)  # wait for random amount of time
                    print("ACK", i + 1, "recieved!!")
                    print("Round Trip time = ", 2 * Time, "ms")
                    print("---------------------------------")
                    if i + 1 != int(len(data) / 4):
                        print("Frame", i + 1, "to be sent!!")
                    if i == int(len(data) / 4) - 1:
                        print(int(len(data) / 4), "frames are successfully transmitted!!!")
            else:
                print("Device",i,"discarded request!")
    print("_________________________________________________________________")
    print("Data recieved by device",destination,":",D[source].content)
    print("_________________________________________________________________")
    print("-----------------------------------------------------------------")

################# hub-switch-hub ##################

if (source<=4 and destination >4) or (source>4 and destination<=4):
    if destination in [5,6,7,8,9]:
        print("Switch forwarded the message to HUB-2")
        print("Connecting to HUB-2 .......")
        m = 0
        while m < 4:
            print(".")
            m += 1
            time.sleep(0.4)

        hub2.hub_values(D[source].MAC, D[source].destMAC, D[source].content)
        print("HUB-2 recieved information successfully from Device :", source)
        print("Source MAC      =", hub2.Source)
        print("Destination MAC =", hub2.Dest)
        print("Message         =", hub2.Data)
        print("-----------------------------------------------------------------")
        print("Now HUB-2 will broadcast the message to devices:5,6,7,8,9")
        for i in range(5,10):
            if i != source:
                if D[i].MAC == hub2.Dest:
                    print("Device", i, "ACCEPTED request.")
                    print("Framing....")
                    while m < 4:
                        print(".")
                        m += 1
                        time.sleep(0.4)
                    while len(data) % 4 != 0:
                        data = '0' + data

                    print("Message will be divided into", int(len(data) / 4), "frames....")
                    print("Frames are sending to reciever using STOP & WAIT protocol......")

                    for i in range(int(len(data) / 4)):
                        frame = data[i * 4:(i + 1) * 4]
                        values = range(10, 30)
                        Time = random.choice(values) / 100
                        time.sleep(Time)  # wait for random amount of time
                        # print(frame)
                        D[destination].content = D[destination].content + frame
                        print("--------------------------------")
                        print("Frame", i, "sent!!")
                        time.sleep(Time)  # wait for random amount of time
                        print("ACK", i + 1, "recieved!!")
                        print("Round Trip time = ", 2 * Time, "ms")
                        print("---------------------------------")
                        if i + 1 != int(len(data) / 4):
                            print("Frame", i + 1, "to be sent!!")
                        if i == int(len(data) / 4) - 1:
                            print(int(len(data) / 4), "frames are successfully transmitted!!!")
                else:
                    print("Device", i, "discarded request!")
        print("_________________________________________________________________")
        print("Data recieved by device", destination, ":", D[source].content)
        print("_________________________________________________________________")
        print("-----------------------------------------------------------------")

    if destination in [0,1,2,3,4]:
        print("Switch forwarded the message to HUB-1")
        print("Connecting to HUB-1 .......")
        m = 0
        while m < 4:
            print(".")
            m += 1
            time.sleep(0.4)

        hub1.hub_values(D[source].MAC, D[source].destMAC, D[source].content)
        print("HUB-1 recieved information successfully from Device :", source)
        print("Source MAC      =", hub1.Source)
        print("Destination MAC =", hub1.Dest)
        print("Message         =", hub1.Data)
        print("-----------------------------------------------------------------")
        print("Now HUB-1 will broadcast the message to devices:0,1,2,3,4")
        for i in range(0,5):
            if i != source:
                if D[i].MAC == hub2.Dest:
                    print("Device", i, "ACCEPTED request.")
                    print("Framing....")
                    while m < 4:
                        print(".")
                        m += 1
                        time.sleep(0.4)
                    while len(data) % 4 != 0:
                        data = '0' + data

                    print("Message will be divided into", int(len(data) / 4), "frames....")
                    print("Frames are sending to reciever using STOP & WAIT protocol......")

                    for i in range(int(len(data) / 4)):
                        frame = data[i * 4:(i + 1) * 4]
                        values = range(10, 30)
                        Time = random.choice(values) / 100
                        time.sleep(Time)  # wait for random amount of time
                        # print(frame)
                        D[destination].content = D[destination].content + frame
                        print("--------------------------------")
                        print("Frame", i, "sent!!")
                        time.sleep(Time)  # wait for random amount of time
                        print("ACK", i + 1, "recieved!!")
                        print("Round Trip time = ", 2 * Time, "ms")
                        print("---------------------------------")
                        if i + 1 != int(len(data) / 4):
                            print("Frame", i + 1, "to be sent!!")
                        if i == int(len(data) / 4) - 1:
                            print(int(len(data) / 4), "frames are successfully transmitted!!!")
                else:
                    print("Device", i, "discarded request!")
        print("_________________________________________________________________")
        print("Data recieved by device", destination, ":", D[source].content)
        print("_________________________________________________________________")
        print("-----------------------------------------------------------------")







########################################################################## gui ################
img=np.zeros((1200,2800,3),np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.rectangle(img,(1200,100), (1300,170), (0,0,255), -1)
cv2.putText(img,"SWITCH", (1200,70), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
#cv2.putText(img,"Message Sent By device "+str()+" to device "+str()+"-->"+str(), (800,200), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
#img = cv2.rectangle(img,(150,800),(250,850),(0,255,0),-1)
cv2.putText(img,"HUB 1", (600,290), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
img=cv2.circle(img,(675,400),60,(0,255,0),-1)
img = cv2.line(img, (1250,170), (675,400), (255, 255, 255), 5)
cv2.putText(img,"HUB 2", (1900,280), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
img=cv2.circle(img,(1925,400),60,(0,255,0),-1)
img = cv2.line(img, (1250,170), (1925,400), (255, 255, 255), 5)

x1=150
y1=800
x2=250
y2=850
k=0
a1=150
b1=880

for i in range(n):
    img = cv2.rectangle(img, (x1 + k, y1), (x2 + k, y2), (100, 100, 100), -1)
    if i<5:
        img = cv2.line(img, (675,400), (200 + k, 800), (255, 255, 255), 5)
        if i==source or i==destination:
            img = cv2.line(img, (675, 400), (200 + k, 800), (255, 0, 0), 5)
    else:
        img = cv2.line(img, (1925, 400), (200 + k, 800), (255, 255, 255), 5)
        if i == source or i == destination:
            img = cv2.line(img, (1925, 400), (200 + k, 800), (255, 0, 0), 5)
    if (source<=4 and destination >=5) or (destination<=4 and source >=5):
        img = cv2.circle(img, (1250,135), 25, (255, 0, 0), -1)



    name = "Device " + str(i)
    cv2.putText(img, name, (a1 + k, b1), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    k=k+250

cv2.putText(img, "STAR-TOPOLOGY", (500,1100), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img, "DATA-LINK LAYER IMPLEMENTATION", (1700,1100), font, 2, (0, 255, 0), 1, cv2.LINE_AA)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()