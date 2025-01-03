import threading as t

# Ordenamiento CRCW (Concurrent Reading Concurrent Writing)

def sort_crcw(L):
    n = len(L)
    win = [0] * n

    def compare(i,j):
        nonlocal win
        if L[i] > L[j]:
            win[i] += 1
        else:
            win[j] += 1

    threads = []

    for i in range(n):
        win[i] = 0

    for i in range(n):
        for j in range(i+1,n):
            thread = t.Thread(target = compare, args = (i,j))
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()

    sorted_array = [0] * n
    print('Win:',win)
    for i in range(n):
        sorted_array[win[i]] = L[i]

    for i in range(n):
        L[i] = sorted_array[i]

def main():
    print('Busqueda CRCW mediante el modulo Threading')
    L = [95,10,6,15]
    print('Arreglo original:',L)

    sort_crcw(L)
    print('Arreglo ordenado:',L)

if __name__ == '__main__':
    main()