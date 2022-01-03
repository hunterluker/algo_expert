import two_sum as program
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1,2,3,4]
        totalSum = 6
        output = program.isTwoSum(array, totalSum)
        self.assertTrue(len(output) == 2)
        self.assertTrue(4 in output)
        self.assertTrue(2 in output)

    def test_case_2(self):
        array = [1,2,3,4]
        totalSum = 3
        output = program.isTwoSum(array, totalSum)
        self.assertTrue(len(output) == 2)
        self.assertTrue(2 in output)
        self.assertTrue(1 in output)

    def test_case_3(self):
        array = [1,2,3,4]
        totalSum = 7
        output = program.isTwoSum(array, totalSum)
        self.assertTrue(len(output) == 2)
        self.assertTrue(4 in output)
        self.assertTrue(3 in output)

    def test_case_4(self):
        array = [8, -2, 23, 1, 10, -5, 2]
        totalSum = 12
        output = program.isTwoSum(array, totalSum)
        self.assertTrue(len(output) == 2)
        self.assertTrue(10 in output)
        self.assertTrue(2 in output)
        

    def test_case_5(self):
        array = [8, -2, 23, 4, 10, -5, 2]
        totalSum = 21
        output = program.isTwoSum(array, totalSum)
        self.assertTrue(len(output) == 2)
        self.assertTrue(23 in output)
        self.assertTrue(-2 in output)

    def test_case_6(self):
        array = [15]
        totalSum = 15
        output = program.isTwoSum(array, totalSum)
        self.assertTrue(len(output) == 0)


if __name__ == '__main__':
    unittest.main()

