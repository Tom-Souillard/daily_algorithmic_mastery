from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Finds the length of the longest increasing subsequence in the given array.

        This function uses a combination of dynamic programming and binary search
        to achieve an optimized solution with O(n log n) time complexity and O(n)
        space complexity. It iterates through the input array, maintaining a sorted
        list of potential candidates for the longest increasing subsequence.

        Args:
            nums: A list of integers.

        Returns:
            The length of the longest strictly increasing subsequence.
        """
        subsequence = []
        for num in nums:
            # Find the index where 'num' should be inserted in 'subsequence'
            index = bisect.bisect_left(subsequence, num)
            # If 'num' is larger than any element in 'subsequence'
            if index == len(subsequence):
                subsequence.append(num)
            else:
                subsequence[index] = num
        return len(subsequence)
