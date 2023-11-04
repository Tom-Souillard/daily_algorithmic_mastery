from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Given an array of integers where each element represents the max number of steps that can be made forward from that element, this function returns the minimum number of jumps to reach the last index.

        Args:
            nums: A list of integers representing the maximum jump length from each index.

        Returns:
            The minimum number of jumps required to reach the last index.
        """
        sauts = 0
        maxAtteint = 0
        finSaut = 0
        for i in range(len(nums) - 1):
            maxAtteint = max(maxAtteint, i + nums[i])
            if i == finSaut:
                sauts += 1
                finSaut = maxAtteint
        return sauts


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]) == 2, "Case 1 Failed"
    assert solution.jump([1, 2, 3, 4, 5]) == 3, "Case 2 Failed"
    print("All test cases passed.")
