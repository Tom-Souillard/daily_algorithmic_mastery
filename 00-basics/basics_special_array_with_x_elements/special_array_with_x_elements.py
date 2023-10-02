from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        Determines if there exists a special number x such that there are exactly x numbers
        in nums that are greater than or equal to x.

        Args:
            nums: List of non-negative integers.

        Returns:
            The special number x if it exists, otherwise -1.
        """
        nums.sort(reverse=True)
        for x in range(1, len(nums) + 1):
            if nums[x - 1] >= x and (x == len(nums) or nums[x] < x):
                return x
        return -1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.specialArray([3, 5]))  # Output: 2
    print(solution.specialArray([0, 0]))  # Output: -1
    print(solution.specialArray([0, 4, 3, 0, 4]))  # Output: 3
    print(solution.specialArray([1, 2, 2, 3, 4, 5]))  # Output: 3
    print(solution.specialArray([10, 2, 3, 4, 7, 8, 9]))  # Output: 5
