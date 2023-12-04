import unittest


class BinarySearch:
    """
    takes unique valued arrays
        # todo rotated arrays\n
        # todo non-unique values

    returns None if target not found

    requires ascending sorted array
    """
    def __init__(self, array, rotated=False):
        if type(array) is not list:
            raise TypeError

        self.array = array
        self.rotated = rotated

    # O(log2 n) time complexity
    # O(1) auxiliary space complexity
    def find(self, target):
        """
        :param target: target to find
        :return: target index or None if not found
        """
        n = len(self.array)
        if n < 3:
            for i in range(n):
                if self.array[i] == target:
                    return i
            else:
                return None

        lo = 0
        hi = n - 1
        while hi > lo:
            mid = lo + (hi - lo) // 2
            element = self.array[mid]
            if element == target:
                return mid
            elif target < element:
                hi = mid - 1
            else:  # target > element:
                lo = mid + 1

        if self.array[lo] == target:
            return lo

        return None

    # O(n * log2 n) time complexity
    def validate(self, target):
        found = self.find(target)
        if not found:
            if target not in self.array:
                return True
        else:  # target in self.array:
            if self.array.index(target) == found:
                return True

        return False


class BinaryTest(unittest.TestCase):
    def type_test_int(self):
        array = 3
        with self.assertRaises(TypeError):
            BinarySearch(array)

    def type_test_float(self):
        array = 3.3
        with self.assertRaises(TypeError):
            BinarySearch(array)

    def type_test_bool(self):
        array = True
        with self.assertRaises(TypeError):
            BinarySearch(array)

    def type_test_none(self):
        array = None
        with self.assertRaises(TypeError):
            BinarySearch(array)
            
    def type_test_dict(self):
        array = {1: 2}
        with self.assertRaises(TypeError):
            BinarySearch(array)

    def type_test_string(self):
        array = '1234'
        with self.assertRaises(TypeError):
            BinarySearch(array)

    def type_test_tuple(self):
        array = (1, 2, 3)
        with self.assertRaises(TypeError):
            BinarySearch(array)
    
    def test_null(self):
        array = []
        target = 0
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_single_match_1(self):
        array = [0]
        target = 0
        actual = BinarySearch(array).find(target)
        expected = 0
        self.assertEqual(expected, actual)

    def test_single_match_2(self):
        array = [1]
        target = 1
        actual = BinarySearch(array).find(target)
        expected = 0
        self.assertEqual(expected, actual)

    def test_single_match_3(self):
        array = [-1]
        target = -1
        actual = BinarySearch(array).find(target)
        expected = 0
        self.assertEqual(expected, actual)

    def test_single_no_match_1(self):
        array = [0]
        target = 1
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_single_no_match_2(self):
        array = [1]
        target = 0
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_single_no_match_3(self):
        array = [-1]
        target = 1
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_single_no_match_4(self):
        array = [1]
        target = -1
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_match_positive_1(self):
        array = list(range(11))
        target = 0
        actual = BinarySearch(array).find(target)
        expected = 0
        self.assertEqual(expected, actual)

    def test_small_match_positive_2(self):
        array = list(range(11))
        target = 5
        actual = BinarySearch(array).find(target)
        expected = 5
        self.assertEqual(expected, actual)

    def test_small_match_positive_3(self):
        array = list(range(11))
        target = 10
        actual = BinarySearch(array).find(target)
        expected = 10
        self.assertEqual(expected, actual)

    def test_small_no_match_positive_1(self):
        array = list(range(11))
        target = -1
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_no_match_positive_2(self):
        array = list(range(11))
        target = 11
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_no_match_positive_3(self):
        array = list(range(11))
        target = 111
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_match_negative_1(self):
        array = list(range(-10, 1, 1))
        target = -10
        actual = BinarySearch(array).find(target)
        expected = 0
        self.assertEqual(expected, actual)

    def test_small_match_negative_2(self):
        array = list(range(-10, 1, 1))
        target = -5
        actual = BinarySearch(array).find(target)
        expected = 5
        self.assertEqual(expected, actual)

    def test_small_match_negative_3(self):
        array = list(range(-10, 1, 1))
        target = 0
        actual = BinarySearch(array).find(target)
        expected = 10
        self.assertEqual(expected, actual)

    def test_small_no_match_negative_1(self):
        array = list(range(-10, 1, 1))
        target = -11
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_no_match_negative_2(self):
        array = list(range(-10, 1, 1))
        target = 1
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_no_match_negative_3(self):
        array = list(range(-10, 1, 1))
        target = 222
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_match_positive_gaps_1_1(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 3
        actual = BinarySearch(array).find(target)
        expected = 0
        self.assertEqual(expected, actual)

    def test_small_match_positive_gaps_1_2(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 7
        actual = BinarySearch(array).find(target)
        expected = 1
        self.assertEqual(expected, actual)

    def test_small_match_positive_gaps_1_3(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 12
        actual = BinarySearch(array).find(target)
        expected = 2
        self.assertEqual(expected, actual)

    def test_small_match_positive_gaps_1_4(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 48
        actual = BinarySearch(array).find(target)
        expected = 3
        self.assertEqual(expected, actual)

    def test_small_match_positive_gaps_1_5(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 99
        actual = BinarySearch(array).find(target)
        expected = 4
        self.assertEqual(expected, actual)

    def test_small_match_positive_gaps_1_6(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 103
        actual = BinarySearch(array).find(target)
        expected = 5
        self.assertEqual(expected, actual)

    def test_small_match_positive_gaps_2_1(self):
        array = [3, 7, 12, 48, 99, 103, 287]
        target = 12
        actual = BinarySearch(array).find(target)
        expected = 2
        self.assertEqual(expected, actual)

    def test_small_match_positive_gaps_2_2(self):
        array = [3, 7, 12, 48, 99, 103, 287]
        target = 48
        actual = BinarySearch(array).find(target)
        expected = 3
        self.assertEqual(expected, actual)

    def test_small_match_positive_gaps_2_3(self):
        array = [3, 7, 12, 48, 99, 103, 287]
        target = 99
        actual = BinarySearch(array).find(target)
        expected = 4
        self.assertEqual(expected, actual)

    def test_small_match_positive_gaps_2_4(self):
        array = [3, 7, 12, 48, 99, 103, 287]
        target = 3
        actual = BinarySearch(array).find(target)
        expected = 0
        self.assertEqual(expected, actual)

    def test_small_match_positive_gaps_2_5(self):
        array = [3, 7, 12, 48, 99, 103, 287]
        target = 287
        actual = BinarySearch(array).find(target)
        expected = 6
        self.assertEqual(expected, actual)

    def test_small_no_match_positive_gaps_1(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 2
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_no_match_positive_gaps_2(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 4
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_no_match_positive_gaps_3(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 102
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_no_match_positive_gaps_4(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 104
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_no_match_positive_gaps_5(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 11
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_no_match_positive_gaps_6(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 13
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_no_match_positive_gaps_7(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 47
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)

    def test_small_no_match_positive_gaps_8(self):
        array = [3, 7, 12, 48, 99, 103]
        target = 49
        actual = BinarySearch(array).find(target)
        expected = None
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
