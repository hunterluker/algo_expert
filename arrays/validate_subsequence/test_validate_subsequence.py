import validate_subsequence as program
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(program.isValidSubsequence(array, sequence))

    def test_case_2(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [8, 6, -1, 10]
        self.assertFalse(program.isValidSubsequence(array, sequence))

    def test_case_3(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 5] 
        self.assertFalse(program.isValidSubsequence(array, sequence))

    def test_case_4(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10, 10]
        self.assertFalse(program.isValidSubsequence(array, sequence))

    def test_case_5(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 25, 6, -1, 8, 10]
        self.assertTrue(program.isValidSubsequence(array, sequence))

    def test_case_6(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 25, 6, -1, 8, 10, 1]
        self.assertFalse(program.isValidSubsequence(array, sequence))

if __name__ == '__main__':
    unittest.main()

