from typing import List
import unittest


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """This function takes a list of integers and sorts them in ascending order first by the
        number of 1's in their binary representation and then by their actual numerical values in
        case of a tie.

        Args:
            arr (List[int]): A list of integers to be sorted.

        Returns:
            List[int]: A new list containing the sorted integers.
        """
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


# Unit tests
class TestSolution(unittest.TestCase):
    def test_sortByBits(self):
        s = Solution()

        self.assertEqual(s.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]), [0, 1, 2, 4, 8, 3, 5, 6, 7])
        self.assertEqual(s.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]),
                         [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
        self.assertEqual(s.sortByBits([10, 100, 1000, 10000]), [10, 100, 1000, 10000])


if __name__ == "__main__":
    unittest.main()
