arr = [2,5,1,8,10,9,3,6,4,7]


def qsort(arr):
    if len(arr) < 1:
        return arr
    leftarr, rightarr = [],[]
    pivot = arr[0]
    for x in arr[1:]:
        if x <= pivot:
            leftarr.append(x)
        else:
            rightarr.append(x)

    return qsort(leftarr) + [pivot] + qsort(rightarr)

print(qsort(arr))
