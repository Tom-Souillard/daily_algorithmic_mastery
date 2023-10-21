from typing import List
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
        Calculate the maximum sum of a non-empty subsequence of the given array `nums`
        such that for every two consecutive integers in the subsequence, the condition
        `j - i <= k` is satisfied.

        Args:
            nums (List[int]): The input array of integers.
            k (int): The maximum allowed distance between indices of two consecutive elements
                     in the subsequence.

        Returns:
            int: The maximum sum of the subsequence that satisfies the given condition.
        """
        max_sum = float('-inf')
        dq = deque()

        for i in range(len(nums)):
            while dq and dq[0] < i - k:
                dq.popleft()

            if dq:
                nums[i] += nums[dq[0]]

            max_sum = max(max_sum, nums[i])

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            if nums[i] > 0:
                dq.append(i)

        return max_sum
