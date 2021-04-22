import threading
import time
def listas():
    element = 0
    lista = [2,7,5,4,9,3,6,8,1,10]
    print('Dado la lista: ', lista)
    for element in lista:
        print(element ,' al cubo : ')
        time.sleep(0.6)
    
def cubito():
    element = 0
    cubos = 1
    suma = 0
    lista = [2,7,5,4,9,3,6,8,1,10]
    cub = []
    for element in lista:
        cubos = element * element * element
        suma = suma + cubos
        cub.append(cubos)
        print('\t\t',cubos, '\n') 
        time.sleep(0.62)
    print(f'La suma de los cubos de la lista {cub} es: {suma}')
##thread = threading.Thread(target=listas)
hilo1 = threading.Thread(target=listas)
hilo2 = threading.Thread(target=cubito)

hilo1.start()
hilo2.start()