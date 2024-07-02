from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Returns the intersection of two integer arrays.

        Args:
            nums1: List of integers.
            nums2: List of integers.

        Returns:
            List containing the intersection of nums1 and nums2.
        """
        compteur1 = Counter(nums1)
        compteur2 = Counter(nums2)
        intersection = []

        for num in compteur1:
            if num in compteur2:
                intersection.extend([num] * min(compteur1[num], compteur2[num]))

        return intersection


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9] or solution.intersect([4, 9, 5],
                                                                                          [9, 4, 9, 8, 4]) == [9, 4]
    print("All tests passed.")
