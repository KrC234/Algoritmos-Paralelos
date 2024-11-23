# Importaciones 
import threading as t
import math as m 

# Busqueda EREW (Exclusive Reading Exclusive Writing)

def broadcastThread(Temp, i, j):
    Temp[j] = Temp[j - pow(2,i-1)]

def minThread(L,i):
    index1 = 2*i
    index2 = 2*i + 1

    if index2 < len(L):
        index1 = 2*i
        index2 = 2*i + 1

        if(L[index1] > L[index2]):
            L[i] = L[index2]
        else:
            L[i] = L[index1]

        
def searchThread(L,Temp, i):
    if L[i] == Temp[i]:
        Temp[i] = i
    else:
        Temp[i] = m.inf

def Broadcast(Temp,x):
    Temp[0] = x
    n = len(Temp)
    k = int(m.log(n,2))

    for i in range(1,k+1):
        threads = []
        for j in range(pow(2,i-1), pow(2,i)):
            thread = t.Thread(target=broadcastThread, args=(Temp,i,j))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

def Min(L):
    n = len(L)
    for j in range(1,int(m.log(n,2))+1):
        threads = []

        for i in range(0, int(n/pow(2,j))):
            thread = t.Thread(target=minThread, args =(L,i))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    return L[0]

def Search(L,x):
    Temp = L[:]
    n = len(L)

    Broadcast(Temp,x)
    threads = []
    for i in range(n):
        thread = t.Thread(target=searchThread, args = (L, Temp, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return Min(Temp)

def main():
    L = [2,-1,23,-4,2,5,-2,0,5,1,5,-5,8,5,3,-6]
    x = 8

    print('Busqueda EREW mediante el modulo Threading')
    print('Lista: ',L)

    print('Elemento a buscar:',x)

    resultado = Search(L,x)

    print(f'El elemento {x} se encuentra en la posición {resultado+1}')

if __name__ == '__main__':
    main()
