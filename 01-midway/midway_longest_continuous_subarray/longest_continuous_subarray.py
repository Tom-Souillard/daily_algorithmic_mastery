class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        """
        Returns the size of the longest non-empty subarray such that the absolute
        difference between any two elements is less than or equal to a given limit.

        Args:
            nums: List of integers representing the input array.
            limit: Maximum allowed absolute difference between any two elements.

        Returns:
            Integer representing the size of the longest valid subarray.
        """
        if not nums:
            return 0

        from collections import deque

        max_deque = deque()
        min_deque = deque()
        left = 0
        longest_length = 0

        for right in range(len(nums)):
            while max_deque and nums[right] > max_deque[-1]:
                max_deque.pop()
            while min_deque and nums[right] < min_deque[-1]:
                min_deque.pop()

            max_deque.append(nums[right])
            min_deque.append(nums[right])

            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1

            longest_length = max(longest_length, right - left + 1)

        return longest_length

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.longestSubarray([8, 2, 4, 7], 4) == 2
    assert solution.longestSubarray([10, 1, 2, 4, 7, 2], 5) == 4
    assert solution.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0) == 3
    print("All tests passed.")
