"""
Write a function that takes in a string of lowercase English-alpahbet letters and returns the index of the string's first non-repeating character.

The first non-repeating character is the first character in a string that occurs only once.

If the input string doesn't have any non-repeating characters, your function should return -1.
"""

# Solution 1
# O(n^2) time | O(1) space
# def firstNonRepeatingCharacter(string):
    # for i in range(len(string)):
        # dupeFound = False
        # for j in range(len(string)):
            # if string[i] == string[j] and i != j:
               # dupeFound = True 
        # if not dupeFound:
            # return i
    # return -1

# Solution 2
# O(n) time | O(1) space
def firstNonRepeatingCharacter(string):
    charCount = {}
    for char in string:
        charCount[char] = charCount.get(char, 0) + 1

    for i in range(len(string)):
        char = string[i]
        if charCount[char] == 1:
            return i

    return -1
        
