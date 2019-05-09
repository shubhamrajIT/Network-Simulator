import numpy as np
import cv2
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

class SWITCH:
    MAC_LIST=[-1,-1,-1,-1,-1]


switch=SWITCH()
D=[]
print("__________________________________________________________________")
print("              DATA-LINK LAYER IMPLEMENTATION ")
print("__________________________________________________________________")
for i in range(5):
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
for i in range(5):
    D[i].MAC=i
    print("MAC address for device", i ,"-> ",i)
print("-----------------------------------------------------------------")
print("Starting service.......")
print("_____________________________________")
print(" INITIAL MAC ADDRESS LIST OF SWITCH")
print("_____________________________________")
print()
print("Devie Name  |   MAC")
print("_____________________")
for i in range(5):
    print("Device",i,"   |   ",switch.MAC_LIST[i])
print("_____________________")

m=0
while m<4:
    print(".")
    m += 1
    time.sleep(0.4)
print("-----------------------------------------------------------------")

while True:

    source=int(input("Enter Source MAC:"))
    destination=int(input("Enter Destination MAC:"))
    data=(input("Enter Data:"))
    print("-----------------------------------------------------------------")
    print("Source device setting up......")
    m=0
    while m<4:
        print(".")
        m += 1
        time.sleep(0.4)

    for i in range(5):
        if i==source:
            D[i].set_values(source,destination,data)
            #print(D[i].MAC)
            #print(D[i].destMAC)
            #print(D[i].content)
    print("Source device initialized successfully")
    print("-----------------------------------------------------------------")
    print("")
    print("___________________________________________________________________")
    print("Framing....")
    while m < 4:
        print(".")
        m += 1
        time.sleep(0.4)
    while len(data) % 4 != 0:
        data = '0' + data

    print("___________________________________________________________________")
    print("Data is sending to switch......")
    m = 0
    while m < 4:
        print(".")
        m += 1
        time.sleep(0.4)

    switch.MAC_LIST[source]=source
    switch.MAC_LIST[destination] = destination
    print("_____________________________________")
    print(" UPDATED MAC ADDRESS LIST OF SWITCH")
    print("_____________________________________")
    print()
    print("Devie Name  |   MAC")

    print("_____________________")
    for i in range(5):
        print("Device",i,"   |   ",switch.MAC_LIST[i])
    print("_____________________")

    if -1 in switch.MAC_LIST:

        #if switch.MAC_LIST.count(-1)==1:
         #   print("Device", destination, "will recieve data! ")

        for i in range(5):
            if i!=source:
                if switch.MAC_LIST[i]==-1:
                    print("Device",i,"will recieve data! ")
        print("Device", destination, "will recieve data! ")
    else:
        print("Data will be transferred from source to destination directly!!")
    ##################
    frame = ""
    print("_______________________________________________________________________")
    print("Message will be divided into",int(len(data)/4),"frames....")
    print("Frames are sending to reciever using STOP & WAIT protocol......")

    canSend=True
    for i in range(int(len(data) / 4)):
        frame = data[i * 4:(i + 1) * 4]
        values = range(10, 30)
        Time = random.choice(values) / 100
        time.sleep(Time)# wait for random amount of time
        #print(frame)
        D[destination].content=D[destination].content+frame
        print("--------------------------------")
        print("Frame",i,"sent!!")
        time.sleep(Time)  # wait for random amount of time
        print("ACK",i+1,"recieved!!")
        print("Round Trip time = ",2*Time,"ms")
        print("---------------------------------")
        if i+1 !=int(len(data)/4):
            print("Frame",i+1,"to be sent!!")
        if i==int(len(data)/4)-1:
            print(int(len(data)/4),"frames are successfully transmitted!!!")



    print("________________________________________________________________________")
    ##################
    #D[destination].content=D[source].content
    print("Data successfully transmitted from device",source,"to device",destination,"!")
    print("Data recieved by device",destination,"->",D[destination].content)
    print("________________________________________________________________________")
###########################################################################################

    img = np.zeros((1200, 2800, 3), np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.circle(img, (700, 200), 63, (0, 0, 255), -1)
    cv2.putText(img, "SWITCH", (670, 120), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img,
                "Message Sent By device " + str(source) + " to device " + str(destination) + "-->" + str(data),
                (800, 200), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    # img = cv2.rectangle(img,(150,800),(250,850),(0,255,0),-1)

    x1 = 150
    y1 = 800
    x2 = 250
    y2 = 850
    k=0
    a1 = 150
    b1 = 880

    for i in range(5):
        img = cv2.rectangle(img, (x1 + k, y1), (x2 + k, y2), (0, 255, 0), -1)
        img = cv2.line(img, (700, 200), (200 + k, 800), (255, 255, 255), 5)

        if i == source or i == destination:
            img = cv2.line(img, (700, 200), (200 + k, 800), (255, 0, 0), 5)

        name = "Device " + str(i)
        cv2.putText(img, name, (a1 + k, b1), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        k = k + 250
        time.sleep(0.4)

    cv2.putText(img, "STAR-TOPOLOGY", (500, 1100), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "DATA-LINK LAYER IMPLEMENTATION", (1700, 1100), font, 2, (0, 255, 0), 2, cv2.LINE_AA)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    # plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
    cmd = input("Press Y to show graphical reprentation:")
    if cmd == "y" or cmd == "Y":
        plt.show()



