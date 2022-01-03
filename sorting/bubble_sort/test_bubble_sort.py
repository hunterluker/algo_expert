import bubble_sort as program
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        self.assertEqual(program.bubbleSort(array), [-1, 1, 5, 6, 8, 10, 22, 25])

    def test_case_2(self):
        array = [5, 1, 2, 5, 10]
        self.assertEqual(program.bubbleSort(array), [1, 2, 5, 5, 10])

    def test_case_3(self):
        array = [5, 1, 2, 5, 6, 13,  8, 10, 6]
        self.assertEqual(program.bubbleSort(array), [1, 2, 5, 5, 6, 6, 8, 10, 13])

    def test_case_4(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(program.bubbleSort(array), [1, 2, 3, 4, 5, 6, 7])

    def test_case_5(self):
        array = [1]
        self.assertEqual(program.bubbleSort(array), [1])

    def test_case_6(self):
        array = [2, 1]
        self.assertEqual(program.bubbleSort(array), [1, 2])

    def test_case_7(self):
        array = [-823, 164, 48, -987, 323, 399, -293, 183, -908, -376, 14, 980, 965, 842, 422, 829, 59, 724, -415, -733, 356, -855, -155, 52, 328, -544, -371, -160, -942, -51, 700, -363, -353, -359, 238, 892, -730, -575, 892, 490, 490, 995, 572, 888, -935, 919, -191, 646, -120, 125, -817, 341, -575, 372, -874, 243, 610, -36, -685, -337, -13, 295, 800, -950, -949, -257, 631, -542, 201, -796, 157, 950, 540, -846, -265, 746, 355, -578, -441, -254, -941, -738, -469, -167, -420, -126, -410, 59]
        self.assertEqual(program.bubbleSort(array), [-987, -950, -949, -942, -941, -935, -908, -874, -855, -846, -823, -817, -796, -738, -733, -730, -685, -578, -575, -575, -544, -542, -469, -441, -420, -415, -410, -376, -371, -363, -359, -353, -337, -293, -265, -257, -254, -191, -167, -160, -155, -126, -120, -51, -36, -13, 14, 48, 52, 59, 59, 125, 157, 164, 183, 201, 238, 243, 295, 323, 328, 341, 355, 356, 372, 399, 422, 490, 490, 540, 572, 610, 631, 646, 700, 724, 746, 800, 829, 842, 888, 892, 892, 919, 950, 965, 980, 995])

if __name__ == '__main__':
    unittest.main()

