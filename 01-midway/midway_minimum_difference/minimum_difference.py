from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        Returns the minimum difference between the largest and smallest value
        after performing at most three moves on the input list of integers.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The minimum difference.
        """
        if len(nums) <= 4:
            return 0

        nums.sort()
        return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minDifference([5, 3, 2, 4]) == 0
    assert solution.minDifference([1, 5, 0, 10, 14]) == 1
    assert solution.minDifference([3, 100, 20]) == 0
    assert solution.minDifference([1, 1, 1, 1]) == 0
    print("All tests passed.")
