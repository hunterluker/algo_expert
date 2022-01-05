"""
Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.
"""

# Solution 1
# O(n) time | O(n) space
# def isPalindrome(string):
    # revStrArr = []
    # for char in reversed(string):
        # revStrArr.append(char)
    # return ''.join(revStrArr) == string

# Solution 2
# O(n^2) time | O(n) space
# def isPalindrome(string):
    # reversedString = ''
    # for i in reversed(range(len(string))):
        # reversedString += string[i]
    # return string == reversedString

# Solution 3
# O(n) time | O(n) space
# def isPalindrome(string, i = 0):
    # j = len(string) - 1 - i
    # return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)
    
# Solution 4
# O(n) time | O(1) space
def isPalindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

