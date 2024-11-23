# Importaciones 
import threading as t 
import math as m 
import time 

def threadAdd(i,j,A):
    if (((2*j) % (m.pow(2,i))) == 0):
        A[2*j] =  A[2*j] + A[((2*j)-((int)(m.pow(2,i-1))))]
    time.sleep(1)

def main():
    print("Suma Erew mediante el modulo Threading")
    A = [0,1,1,1,1,1,1,1,1]
    print(A)

    t1 = time.time() # definicion del tiempo de inicio 
    n = len(A) - 1
    threads = [] # arreglo para el almacenamiento de hilos 
    log = int(m.log(n,2))

    '''
    Se emulan ciclos paralelos mediante ciclos repetitivos 
    Los la razón de uso de hilos se da mediante una función logaritmica
    Se inicializan los hilos en un conjunto y después se finalizan
    '''
    for i in range(1,log+1):

        for j in range(1,(int)(n/2)+1):
            thread = t.Thread(target = threadAdd, args = (i,j,A))
            threads.append(thread)
            thread.start()

        for hilo in threads:
            hilo.join()
        
        print(A)
    t2 = time.time()
    print(t2-t1) # Definición del tiempo final 

if __name__ ==  '__main__':
    main()
