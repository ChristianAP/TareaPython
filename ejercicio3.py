import threading
import time
def factorial():
    nro = int(input("Ingrese un número: "))
    facto = 1
    nro2= nro
    while nro2 > 0:
        facto = facto * nro2
        print(nro2, '\tx')
        nro2-=1
        time.sleep(0.4)
    print('-----------------')  
    print(f"El factorial de {nro} es : {facto}", '\n')

factorial = threading.Thread(target=factorial)
factorial.start()
