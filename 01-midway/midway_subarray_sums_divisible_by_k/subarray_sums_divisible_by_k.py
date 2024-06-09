class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        """
        Returns the number of non-empty subarrays that have a sum divisible by k.

        Args:
            nums: A list of integers.
            k: An integer representing the divisor.

        Returns:
            An integer representing the number of subarrays with sums divisible by k.
        """
        prefix_sums = {0: 1}
        total = 0
        result = 0

        for nombre in nums:
            total += nombre
            reste = total % k
            if reste < 0:
                reste += k
            if reste in prefix_sums:
                result += prefix_sums[reste]
                prefix_sums[reste] += 1
            else:
                prefix_sums[reste] = 1

        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.subarraysDivByK([4,5,0,-2,-3,1], 5) == 7
    assert solution.subarraysDivByK([5], 9) == 0
    print("All tests passed.")
