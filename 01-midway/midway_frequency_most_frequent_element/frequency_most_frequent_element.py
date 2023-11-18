from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        Finds the maximum frequency of an element in the given array after performing
        at most k increments on any of the array elements.

        Args:
        nums (List[int]): The input array.
        k (int): The maximum number of allowed increments.

        Returns:
        int: The maximum possible frequency of any element in the array after
             performing the operations.

        Complexity:
        Time: O(n log n) due to sorting, where n is the length of the array.
        Space: O(1) additional space complexity.
        """
        nums.sort()
        left = 0
        max_freq = 0
        somme = 0

        for right in range(len(nums)):
            somme += nums[right]

            # Check if the current window exceeds the limit
            while nums[right] * (right - left + 1) - somme > k:
                somme -= nums[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)

        return max_freq


# Example usage
sol = Solution()
print(sol.maxFrequency([1, 2, 4], 5))  # Output: 3
print(sol.maxFrequency([1, 4, 8, 13], 5))  # Output: 2
print(sol.maxFrequency([3, 9, 6], 2))  # Output: 1
