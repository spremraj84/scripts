#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        number = arr[i]
        window = i
        while number < arr[window-1] and window > 0:
            tmp = arr[window-1]
            arr[window-1] = arr[window]
            arr[window] = tmp
        print(*arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
