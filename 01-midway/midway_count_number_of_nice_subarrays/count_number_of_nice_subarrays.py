class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of subarrays with exactly k odd numbers.

        Args:
            nums: A list of integers representing the input array.
            k: An integer representing the exact count of odd numbers required in the subarray.

        Returns:
            An integer representing the number of subarrays with exactly k odd numbers.
        """
        def atMostKOdd(nums: list[int], k: int) -> int:
            count = 0
            left = 0
            result = 0

            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    k -= 1

                while k < 0:
                    if nums[left] % 2 != 0:
                        k += 1
                    left += 1

                result += right - left + 1

            return result

        return atMostKOdd(nums, k) - atMostKOdd(nums, k - 1)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.numberOfSubarrays([1,1,2,1,1], 3) == 2
    assert solution.numberOfSubarrays([2,4,6], 1) == 0
    assert solution.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2) == 16
    print("All tests passed.")
