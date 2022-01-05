import palindrome_check as program
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "racecar"
        self.assertTrue(program.isPalindrome(string))

    def test_case_2(self):
        string = "abcba"
        self.assertTrue(program.isPalindrome(string))

    def test_case_3(self):
        string = "a"
        self.assertTrue(program.isPalindrome(string))

    def test_case_4(self):
        string = "ab"
        self.assertFalse(program.isPalindrome(string))

    def test_case_5(self):
        string = "bababab"
        self.assertTrue(program.isPalindrome(string))

    def test_case_6(self):
        string = "abcdefghihgfedcba"
        self.assertTrue(program.isPalindrome(string))

    def test_case_7(self):
        string = "abcdefghijhgfedcba"
        self.assertFalse(program.isPalindrome(string))

if __name__ == '__main__':
    unittest.main()

