"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.
"""

# Soltuion 1
# O(n^2) time | O(1) space
# def isTwoSum(array, totalSum):
    # for i in range(len(array) - 1):
        # for j in range(i + 1, len(array)):
            # if array[i] + array[j] == totalSum:
                # return [array[i], array[j]]
    # return []

# Soltuion 2
# O(n) time | O(n) space
def isTwoSum(array, totalSum):
    nums = {}
    for num in array:
        match = totalSum - num
        if match in nums:
            return [match, num]
        else:
            nums[num] = True
    return []
        
# Soltuion 3
# O(nlog(n)) time | O(1) space
# def isTwoSum(array, totalSum):
    # array.sort()
    # left = 0
    # right = len(array) - 1
    # while left < right:
        # sum = array[left] + array[right]
        # if sum == totalSum:
            # return [array[left], array[right]]
        # elif sum < totalSum:
            # left += 1
        # elif sum > totalSum:
            # right -= 1
    # return []
        
