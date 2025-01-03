import threading as t

# Busqueda CRCW (Concurrent Reading Exclusive Writing)

def min_crcw(L):
    n = len(L)
    win = [0] * n

    def compare(i,j):
        nonlocal win
        if L[i] > L[j]:
            win[i] = 1
        else: 
            win[j] = 1

    def find_min():
        nonlocal win
        for i in range(n):
            if win[i] == 0:
                return i
            
    threads = []

    for i in range(n):
        win[i] = 0

    for i in range(n):
        for j in range(i + 1, n):
            thread = t.Thread(target = compare, args = (i,j))
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()

    index_min =  find_min()
    print('win:',win)

    return L[index_min]


def main():
    print('Busqueda CRCW mediante el modulo Threading')

    L = [95,10,6,15]

    print('Arreglo inicial:',L)

    resultado = min_crcw(L)
    print('Valor minimo:',resultado)

if __name__ == '__main__':
    main()