# Importaciones 
import math as m 
import threading as t
import time 

# Suma CREW (Concurrent Reading Exclusive Writing)

def threadAdd(i,j,A):
    A[j] = A[j] + A[j - pow(2,i-1)]
    time.sleep(1)

def main():
    print('Suma CREW mediante el modulo Threading')
    A = [0,1,1,1,1,1,1,1,1]

    t1 = time.time()
    print(A)

    n = len(A)-1 
    threads = []
    log = int(m.log(n,2))

    for i in range(1,log+1):
        for j in range(n, pow(2,i-1), -1):
            thread = t.Thread(target=threadAdd, args =(i,j,A))
            threads.append(thread)
            thread.start()

        for hilo in threads:
            hilo.join()
        print(A)

    t2 = time.time()
    print(t2 - t1)

if __name__ == '__main__':
    main()
