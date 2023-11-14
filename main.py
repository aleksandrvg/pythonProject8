import random
import time

def arrRandmizer(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(1, 1000000))
    return arr

def bubleSort(arr):
    for i in range(len(arr)):
        for z in range(len(arr)-1):
            if arr[z] < arr[z+1]:
                arr[z], arr[z+1] = arr[z+1], arr[z]

arr = arrRandmizer(100)

startTime = time.time()
bubleSort(arr)
endTime = time.time()
print('Сортировка пузырьком')
print(arr)
print(endTime-startTime)


def shakerSort(arr):
    N = len(arr)

    Left = 0
    Right = N - 1

    while Left < Right:
        for i in range(Right, Left, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        for i in range(Left + 1, Right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        Right -= 1
        Left += 1

startTime = time.time()
shakerSort(arr)
endTime = time.time()
print('Шейкерная сортировка')
print(arr)
print(endTime-startTime)


def insertSort(arr):
    N = len(arr)
    for i in range(N):
        arr.append(random.randint(0, 100))
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

startTime = time.time()
insertSort(arr)
endTime = time.time()
print('Сортировка вставками')
print(arr)
print(endTime-startTime)
