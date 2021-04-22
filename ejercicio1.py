import threading  
import time
def Lista():
    i = 0
    j = 10
    while i < 10:
        print(i)
        time.sleep(0.5)
        i+=1
    while j >= 0:
        print(j) 
        time.sleep(0.5)
        j-=1


Thread = threading.Thread(target = Lista)
Thread.start()
        
