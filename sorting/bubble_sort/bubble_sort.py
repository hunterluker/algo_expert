"""
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort algorithm to sort the array.
"""

# Soltuion 1
# O(n^2) time | O(1) space 
# def bubbleSort(array):
    # for i in range(len(array) - 1):
        # for j in range(i + 1, len(array)):
            # tmp = array[i]
            # if array[i] > array[j]:
                # array[i] = array[j]
                # array[j] = tmp
    # return array

# Soltuion 2
# O(n^2) time | O(1) space 
def bubbleSort(array):
    isSorted = False
    count = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - count):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
        count += 1
    return array

def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]

