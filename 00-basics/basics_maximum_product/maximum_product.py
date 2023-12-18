from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        """
        Calculate the maximum product difference between two pairs from a list.

        Args:
        nums: A list of integers.

        Returns:
        The maximum product difference between two pairs (a, b) and (c, d) in nums,
        defined as (a * b) - (c * d).

        Time Complexity: O(n log n), where n is the length of nums.
        Space Complexity: O(1), no extra space required besides input.
        """
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
