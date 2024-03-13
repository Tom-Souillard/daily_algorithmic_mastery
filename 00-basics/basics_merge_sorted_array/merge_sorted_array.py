from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 as one sorted array.

        Args:
        nums1 (List[int]): The first list of numbers with extra space at the end.
        m (int): The number of initialized elements in nums1.
        nums2 (List[int]): The second list of numbers.
        n (int): The number of initialized elements in nums2.
        """
        index_total = m + n - 1
        index1 = m - 1
        index2 = n - 1
        while index2 >= 0:
            if index1 >= 0 and nums1[index1] > nums2[index2]:
                nums1[index_total] = nums1[index1]
                index1 -= 1
            else:
                nums1[index_total] = nums2[index2]
                index2 -= 1
            index_total -= 1

# Test cases
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print("Expected: [1,2,2,3,5,6]", "Got:", nums1)

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    print("Expected: [1]", "Got:", nums1)

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print("Expected: [1]", "Got:", nums1)
