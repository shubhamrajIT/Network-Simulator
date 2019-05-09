import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

class device:
    MAC=0
    destMAC=0
    content=0
    def set_values(self,source,dest,data):
        self.MAC=source
        self.destMAC=dest
        self.content=data

class BRIDGE:
    port1=[0,1,2]
    port2=[3,4,5]

D=[]
print("__________________________________________________________________")
print("              DATA-LINK LAYER IMPLEMENTATION ")
print("__________________________________________________________________")
for i in range(6):
    D.append(device())
print("-----------------------------------------------------------------")
print("6 Devices created")
print("-----------------------------------------------------------------")
print("Setting MAC address for each device")
m=0
while m<4:
    print(".")
    m+=1
    time.sleep(0.4)
print("-----------------------------------------------------------------")
for i in range(6):
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
data=int(input("Enter Data:"))
print("-----------------------------------------------------------------")
print("Source device setting up......")
m=0
while m<4:
    print(".")
    m += 1
    time.sleep(0.4)

for i in range(6):
    if i==source:
        D[i].set_values(source,destination,data)
        #print(D[i].MAC)
        #print(D[i].destMAC)
        #print(D[i].content)
print("Source device initialized successfully")
print("-----------------------------------------------------------------")
b=BRIDGE()

if source in [0,1,2] and destination in [3,4,5]:
    for i in range(0,3):
        if i!=source:
            print("Device",i,"discarded the request!")
    print()
    print("Bridge forwarded the request to devices 3,4,5")
    print()
    for i in range(3,6):
        if i==destination:
            D[i].content=data
            print("Device",i,"accepted the request!")
        else:
            print("Device", i, "discarded the request!")

if source in [3,4,5] and destination in [0,1,2]:
    for i in range(3,6):
        if i!=source:
            print("Device",i,"discarded the request!")
    print()
    print("Bridge forwarded the request to devices 0,1,2")
    print()
    for i in range(0,3):
        if i==destination:
            D[i].content=data
            print("Device",i,"accepted the request!")
        else:
            print("Device", i, "discarded the request!")


if source in [0,1,2] and destination in [0,1,2]:
    print("Bridge dicarded the request!")
    for i in range(0,3):
        if i!=source:
            if i==destination:
                print("Device", i, "accepted the request!")
                D[i].content = data
            else:
                print("Device", i, "discarded the request!")

if source in [3,4,5] and destination in [3,4,5]:
    print("Bridge dicarded the request!")
    for i in range(3,6):
        if i!=source:
            if i==destination:
                print("Device", i, "accepted the request!")
                D[i].content = data
            else:
                print("Device", i, "discarded the request!")

####################
print("_________________________________________________________________")
print("Data transferred by device",source,"to device",destination,":",D[destination].content)
print("_________________________________________________________________")
print("-----------------------------------------------------------------")
#######################################################################

img=np.zeros((1200,2800,3),np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.line(img, (150,600), (2250,600), (255, 255, 255), 5)
x1=250
y1=600
x2=250
y2=700
k=0
j=0

for i in range(7):

    if i==3:
        img = cv2.rectangle(img, (1100,570), (1300,630), (0, 255, 0), -1)
        cv2.putText(img, "BRIDGE", (1150, 500), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        if (source in [0,1,2] and destination in [3,4,5]) or (source in [3,4,5] and destination in [0,1,2]):
            img = cv2.circle(img, (1200, 600), 20, (255, 0, 0), -1)
    else:
        dev = "Device " + str(j)
        if i%2==0:
            img = cv2.line(img, (250+k, 600), (250+k, 700), (255, 255, 255), 5)
            img = cv2.circle(img, (x1+k, 600), 10, (255, 0, 0), -1)
            img = cv2.circle(img, (x1 + k, 700),63, (0, 0, 255), -1)
            cv2.putText(img, dev, (200+k, 800), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

            if source==j or destination==j:
                img = cv2.circle(img, (x1 + k, 700), 30, (0, 255, 0), -1)

            j += 1
        else:
            img = cv2.line(img, (250+k, 600), (250+k, 500), (255, 255, 255), 5)
            img = cv2.circle(img, (x1+k, 600), 10, (255, 0, 0), -1)
            img = cv2.circle(img, (x1 + k, 500),63, (0, 0, 255), -1)
            cv2.putText(img,dev, (200+k, 400), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

            if source==j or destination==j:
                img = cv2.circle(img, (x1 + k, 500), 30, (0, 255, 0), -1)

            j += 1
    k+=320

cv2.putText(img, "DATA-LINK LAYER IMPLEMENTATION", (1700,1100), font, 2, (0, 255, 0), 2, cv2.LINE_AA)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
cmd=input("Press Y to show graphical reprentation:")
if cmd=="y" or cmd=="Y":
    plt.show()
else:
    exit(1)
