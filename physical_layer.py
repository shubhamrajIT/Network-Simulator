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

class HUB:
    Source=0
    Dest=0
    Data=0
    def hub_values(self,source,dest,data):
        self.Source=source
        self.Dest=dest
        self.Data=data

####################### MAIN  ###########
D=[]
print("__________________________________________________________________")
print("              PHYSICAL LAYER IMPLEMENTATION ")
print("__________________________________________________________________")
n=int(input("Enter Number of devices you want to add:"))
for i in range(n):
    D.append(device())
print("-----------------------------------------------------------------")
print(n,"Devices created")
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
data=int(input("Enter Data:"))
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
print("Connecting to HUB.......")
m=0
while m<4:
    print(".")
    m += 1
    time.sleep(0.4)
hub=HUB()
hub.hub_values(D[source].MAC,D[source].destMAC,D[source].content)
print("HUB recieved information successfully from Device :",source)
print("Source MAC      =",hub.Source)
print("Destination MAC =",hub.Dest)
print("Message         =",hub.Data)
print("-----------------------------------------------------------------")
print("HUB is sending message to other",n-1,"devices......")
m=0
while m<4:
    print(".")
    m += 1
    time.sleep(0.4)
print("_________________________________________________________________")

for i in range(n):
    if i!=source:
        if D[i].MAC==hub.Dest:
            D[i].content=hub.Data
            print("Device", i, "ACCEPTED request.")
        else:
            print("Device",i,"discarded request!")
print("_________________________________________________________________")
print("Data recieved by device",destination,":",D[source].content)
print("_________________________________________________________________")
print("-----------------------------------------------------------------")

img=np.zeros((1200,2800,3),np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.circle(img,(700,200), 63, (0,0,255), -1)
cv2.putText(img,"HUB", (670,120), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img,"Message Sent By device "+str(hub.Source)+" to device "+str(hub.Dest)+"-->"+str(hub.Data), (800,200), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
#img = cv2.rectangle(img,(150,800),(250,850),(0,255,0),-1)

x1=150
y1=800
x2=250
y2=850
k=0
a1=150
b1=880

for i in range(n):
    img = cv2.rectangle(img, (x1+k,y1), (x2+k,y2), (0, 255, 0), -1)
    img = cv2.line(img, (700, 200), (200 + k, 800), (255, 255, 255), 5)

    if i==source or i==destination:
        img = cv2.line(img, (700, 200), (200 + k, 800), (255, 0, 0), 5)

    name = "Device " + str(i)
    cv2.putText(img, name, (a1 + k, b1), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    k=k+250
    time.sleep(0.4)

cv2.putText(img, "STAR-TOPOLOGY", (500,1100), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img, "PHYSICAL LAYER IMPLEMENTATION", (1700,1100), font, 2, (0, 255, 0), 2, cv2.LINE_AA)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
cmd=input("Press Y to show graphical reprentation:")
if cmd=="y" or cmd=="Y":
    plt.show()
else:
    exit(1)
