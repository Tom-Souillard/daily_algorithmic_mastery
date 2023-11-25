class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        Calculate the sum of absolute differences in a sorted array.

        Args:
        nums (List[int]): A sorted list of integers.

        Returns:
        List[int]: A list where each element is the sum of absolute differences
                   between that element and every other element in the input list.

        The function uses prefix sums to efficiently calculate the result. The time complexity is O(n)
        and space complexity is O(n), where n is the length of the input list.
        """
        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        result = []
        for i in range(n):
            left_sum = nums[i] * i - prefix_sum[i]
            right_sum = prefix_sum[n] - prefix_sum[i + 1] - nums[i] * (n - i - 1)
            result.append(left_sum + right_sum)

        return result
