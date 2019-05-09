import random
import string
import time
import dijkstras2
import dijkstras

print("*****************************   DYNAMIC ROUTING(OSPF) IMPLEMENTATION  ***************************************************")

################################################################

########################################################################################


class device:
    MAC_source=""
    IP_source=""
    Subnet_mask=""
    gateway=""
####################
class router:
    MAC_source=""
    name=""

    def __init__(self):
        self.interface={}
        self.routing_table=[]
        self.nidlist=[]
        self.directly_connected=[]
        self.shortest_route={}


choice=input("Press 'Yes' to Run packet tracer for default configuration or Press 'No' for generalise configuration:")
if choice== "yes":
    d = 6
    n = 3
else:
    d=int(input("Enter no. of End devices:"))
    n=int(input("Enter no. of Routers:"))

PC=[]
for i in range(d):
    PC.append(device())

R=[]
for i in range(n):
    R.append(router())



def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

if choice=="yes" :
#########  MAC configurartion ##########
    PC[0].MAC_source="B2:34:55:10:22:10"
    PC[1].MAC_source="A1:15:55:10:21:11"
    PC[2].MAC_source="B3:33:55:10:22:12"
    PC[3].MAC_source="C2:35:55:10:20:13"
    PC[4].MAC_source="A4:39:55:10:18:14"
    PC[5].MAC_source="C1:37:55:10:30:15"

    R[0].MAC_source="D0:30:55:10:22:CC"
    R[1].MAC_source="D1:31:54:11:21:DD"
    R[2].MAC_source="D2:32:53:12:22:FF"
else:
    for i in range(d):

        PC[i].MAC_source=random_char(12)
        #print(PC[i].MAC_source)
    for i in range(n):
        R[i].MAC_source=random_char(12)
        #print(R[i].MAC_source)
############################################

print("Type 'pcconfig' to configure IP addresses of devices:")
if(input()=="pcconfig"):
    for i in range(d):
        print("Configuring PC[",i,"]...")
        PC[i].IP_source=input("Enter IP address:")
        ip=PC[i].IP_source
        m = 0
        c = ''
        while (ip[m] != '.'):
            c = c + ip[m]
            m = m + 1

        if(int(c)>=0 or int(c)<=127):
            PC[i].Subnet_mask = "255.0.0.0"
        elif(int(c) >= 128 or int(c) <= 191):
            PC[i].Subnet_mask = "255.255.0.0"
        else:
            PC[i].Subnet_mask = "255.255.255.0"
        PC[i].gateway = input("Enter Gateway:")
else:
        PC[0].IP_source="192.168.1.1"
        PC[0].Subnet_mask="255.255.255.0"
        PC[0].gateway="192.168.1.100"

        PC[1].IP_source = "192.168.1.2"
        PC[1].Subnet_mask = "255.255.255.0"
        PC[1].gateway = "192.168.1.100"

        PC[2].IP_source = "192.168.2.1"
        PC[2].Subnet_mask = "255.255.255.0"
        PC[2].gateway = "192.168.2.100"

        PC[3].IP_source = "192.168.2.2"
        PC[3].Subnet_mask = "255.255.255.0"
        PC[3].gateway = "192.168.2.100"

        PC[4].IP_source = "192.168.3.1"
        PC[4].Subnet_mask = "255.255.255.0"
        PC[4].gateway = "192.168.3.100"

        PC[5].IP_source = "192.168.3.2"
        PC[5].Subnet_mask = "255.255.255.0"
        PC[5].gateway = "192.168.3.100"



print(" --------------------------------------------------------------------------------------------------")
print("   All PC's configured")
print("|_________________________________________________________________________________________________|")
print("| PC name |      MAC address    |    IP address         |  Subnet Mask       |        Gateway     |")
for i in range(d):

    print("|_________________________________________________________________________________________________|")
    print("|",i,"      |",PC[i].MAC_source,"  |     ",PC[i].IP_source,"     |",PC[i].Subnet_mask,"     |   ",PC[i].gateway,"  |")
    print("|_________________________________________________________________________________________________|")

print("*********************************************************************************************************")
print("Type 'rconfig' to configure Routers:")
if(input()=="rconfig"):
    for i in range(n):
        print("Configuring Router[",i,"]...")
        intf=int(input("Enter number of interfaces:"))
        for j in range(intf):
            print("Enter IP for interface:", j)
            ip = input()
            R[i].interface[j] = ip

else:
    R[0].interface[0] = "192.168.1.100"
    R[0].interface[1] = "192.168.2.100"
    R[0].interface[2] = "192.168.6.1"
    R[0].interface[3] = "192.168.4.1"

    R[1].interface[0] = "192.168.6.2"
    R[1].interface[1] = "192.168.3.100"
    R[1].interface[2] = "192.168.5.2"

    R[2].interface[0] = "192.168.4.2"
    R[2].interface[1] = "192.168.5.1"

print("------------------------------------------------------------------------------------------")
print("All routers configured.....")
print()
for i in range(n):
    print("________________________________________________________________________________________________________")
    print("Router",i,":(interface,ip)->",R[i].interface)

print("*********************************************************************************************************")

for i in range(n):
        print("----------------------------Router ",i,"---------------------------------------------------------")
        iplist=list(R[i].interface.values())   #these are directly connected ip addresses

        if PC[i].Subnet_mask=="255.255.255.0":
            for j in range(len(iplist)):
                R[i].directly_connected.append(iplist[j][0:9]+".0")
        if PC[i].Subnet_mask=="255.255.0.0":
            for j in range(len(iplist)):
                R[i].directly_connected.append(iplist[j][0:7]+".0.0")
        elif PC[i].Subnet_mask=="255.0.0.0":
            for j in range(len(iplist)):
                R[i].directly_connected.append(iplist[j][0:2]+".0.0.0")

        print()
        print('Directly connected list for Router',i,R[i].directly_connected)  ## these are nids
        print("--------------------------------------------------------------------------------------------------")

print("_____________________________________________________________________________________________________________")


all_nids=[]
for i in range(n):
    for j in range(len(R[i].directly_connected)):
        all_nids.append(R[i].directly_connected[j])
#print(all_nids)
all_nids=list(set(all_nids))


c1=int(input("Assign Cost between R[0] and R[1]:"))
c2=int(input("Assign Cost between R[1] and R[2]:"))
c3=int(input("Assign Cost between R[2] and R[0]:"))

graph={'a':{'b':c1,'c':c3},'b':{'a':c1,'c':c2},'c':{'a':c3,'b':c2}}

R[0].shortest_route=dijkstras2.dijkstra(graph,'a')

graph={'a':{'b':c1,'c':c3},'b':{'a':c1,'c':c2},'c':{'a':c3,'b':c2}}

R[1].shortest_route=dijkstras2.dijkstra(graph,'b')

graph={'a':{'b':c1,'c':c3},'b':{'a':c1,'c':c2},'c':{'a':c3,'b':c2}}

R[2].shortest_route=dijkstras2.dijkstra(graph,'c')

print("Cost has been assigned between each router......")
print("------------------------------------------------------------------------------------------")
print("Shortest path when Router 0 is root node:",R[0].shortest_route)
print("Shortest path when Router 1 is root node:",R[1].shortest_route)
print("Shortest path when Router 2 is root node:",R[2].shortest_route)
print("------------------------------------------------------------------------------------------")


a=input("Enter Source Router:")
b=input("Enter Destination Router:")
graph={'a':{'b':c1,'c':c3},'b':{'a':c1,'c':c2},'c':{'a':c3,'b':c2}}
dijkstras.dijkstra(graph,a,b)