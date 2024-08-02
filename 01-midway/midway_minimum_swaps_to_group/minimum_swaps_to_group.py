from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        Returns the minimum number of swaps required to group all 1's together in a circular array.

        Args:
            nums (List[int]): The input binary circular array.

        Returns:
            int: The minimum number of swaps required.
        """
        total_uns = nums.count(1)
        n = len(nums)
        if total_uns == 0:
            return 0

        fenetre = sum(nums[:total_uns])
        max_uns = fenetre

        for i in range(1, n):
            fenetre = fenetre - nums[i - 1] + nums[(i + total_uns - 1) % n]
            max_uns = max(max_uns, fenetre)

        return total_uns - max_uns

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minSwaps([0,1,0,1,1,0,0]) == 1
    assert solution.minSwaps([0,1,1,1,0,0,1,1,0]) == 2
    assert solution.minSwaps([1,1,0,0,1]) == 0
    assert solution.minSwaps([0,0,0,0,0]) == 0
    assert solution.minSwaps([1,1,1,1,1]) == 0
    print("All tests passed.")
