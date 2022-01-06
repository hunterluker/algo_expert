import first_non_repeating_character as program
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "abcdaf"
        expected = 1
        actual = program.firstNonRepeatingCharacter(string)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        string = "abab"
        expected = -1
        actual = program.firstNonRepeatingCharacter(string)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        string = "abcdabcdf"
        expected = 8
        actual = program.firstNonRepeatingCharacter(string)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        string = "a"
        expected = 0
        actual = program.firstNonRepeatingCharacter(string)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        string = "abcdefghijklmnopabcdefghijklmnop"
        expected = -1
        actual = program.firstNonRepeatingCharacter(string)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

