#! /usr/bin/python3

arr = [2,5,1,8,10,9,3,6,4,7]

left = 0
right = len(arr)

print("the given list is: ", *arr)

def mergesort(arr):
    result = []
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    leftarr,rightarr= mergesort(arr[:mid]), mergesort(arr[mid:])

    result = merge(leftarr,rightarr, arr.copy())

    return result

def merge(leftarr,rightarr, merged):
    i,j = 0,0
    while i < len(leftarr) and j < len(rightarr):
        if leftarr[i] <= rightarr[j]:
            merged[i+j] = leftarr[i]
            i+=1
        else:
            merged[i+j] = rightarr[j]
            j+=1

    for i in range(i, len(leftarr)):
        merged[i+j] = leftarr[i]
    for j in range(j, len(rightarr)):
        merged[i+j] = rightarr[j]

    return merged



print("the sorted list is: ", *mergesort(arr))
