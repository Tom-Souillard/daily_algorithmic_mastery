class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        """
        Computes the minimum number of k-bit flips required so that there are no 0s in the binary array.

        Args:
            nums: A binary array where 0s and 1s are represented as integers.
            k: The length of subarrays for k-bit flips.

        Returns:
            The minimum number of k-bit flips needed to make the array all 1s. Returns -1 if it's not possible.

        """
        n = len(nums)
        flips = 0
        flipped = [0] * n
        curr_flips = 0

        for i in range(n):
            if i >= k:
                curr_flips -= flipped[i - k]
            if (nums[i] + curr_flips) % 2 == 0:
                if i + k > n:
                    return -1
                flips += 1
                curr_flips += 1
                flipped[i] = 1

        return flips


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minKBitFlips([0, 1, 0], 1) == 2
    assert solution.minKBitFlips([1, 1, 0], 2) == -1
    assert solution.minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3) == 3
    print("All tests passed.")
