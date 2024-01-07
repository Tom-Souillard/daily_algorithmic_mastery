class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Calculate the number of arithmetic subsequences in an array.

        This function computes the total number of arithmetic subsequences
        in the given list of integers. A subsequence is considered arithmetic
        if it consists of at least three elements and the difference between
        any two consecutive elements is the same.

        Args:
        nums (List[int]): A list of integers.

        Returns:
        int: The total number of arithmetic subsequences in the list.

        Example:
            nums = [2, 4, 6, 8, 10]
            -> returns 7
        """
        total = 0
        dp = [collections.defaultdict(int) for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                if dp[j][diff]:
                    total += dp[j][diff]
        return total
