"""
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
"""

# Solution 1
# O(n) time | O(1) space - where n is the length of the array
def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

# Solution 2
# O(n) time | O(1) space 
# def isValidSubsequence(array, sequence):
    # seqIdx = 0
    # for num in array:
        # if seqIdx == len(sequence):
            # break
        # if num == sequence[seqIdx]:
            # seqIdx += 1
    # return seqIdx == len(sequence)
