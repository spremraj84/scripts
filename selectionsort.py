#!/bin/python3

arr = [2,5,1,8,10,9,3,6,4,7]

def selectionsort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(min+1, len(arr)):
            if(arr[min] > arr[j]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    print(*arr)


selectionsort(arr)
