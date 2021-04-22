import threading
import time


def Leopardo1():
    nro = 0
    while nro < 5:
        print("- Leopardo 1 -") 
        nro+=1
        time.sleep(0.3)
def Leopardo2():
    nro = 0
    while nro < 5:
        print("- Leopardo 2 -") 
        nro+=1
        time.sleep(0.3)
def Leopardo3():
    nro = 0
    while nro < 5:
        print("- Leopardo 3 -") 
        nro+=1
        time.sleep(0.3)
def Leopardo4():
    nro = 0
    while nro < 5:
        print("- Leopardo 4 -") 
        nro+=1
        time.sleep(0.3)
    print("AH GANADO¡¡¡¡¡¡")


leopa1 = threading.Thread(target= Leopardo1)
leopa2 = threading.Thread(target= Leopardo2)
leopa3 = threading.Thread(target= Leopardo3)
leopa4 = threading.Thread(target= Leopardo4)
leopa1.start()
leopa2.start()
leopa3.start()
leopa4.start()