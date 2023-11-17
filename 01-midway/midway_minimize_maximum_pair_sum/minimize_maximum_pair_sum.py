class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
        Minimizes the maximum pair sum by optimally pairing elements of the array.

        Args:
        nums (List[int]): The input array of integers.

        Returns:
        int: The minimized maximum pair sum.
        """
        nums.sort()  # In-place sorting to minimize memory usage
        n = len(nums)
        somme_max = 0
        for i in range(n // 2):
            somme_max = max(somme_max, nums[i] + nums[n - 1 - i])
        return somme_max