#!/usr/bin/python3

"""
Bubble Sort.
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


data = [64, 34, 25, 12, 22, 11, 90]

print("Before: ", data)
bubble_sort(data)
print("After : ", data)
