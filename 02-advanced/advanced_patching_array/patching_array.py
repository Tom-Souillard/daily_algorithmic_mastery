class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        """
        Calculate the minimum number of patches required to cover the range [1, n].

        Args:
            nums (List[int]): A sorted list of integers.
            n (int): The upper limit of the range to be covered.

        Returns:
            int: The minimum number of patches required.
        """
        couverture = 0
        patchs = 0
        i = 0
        while couverture < n:
            if i < len(nums) and nums[i] <= couverture + 1:
                couverture += nums[i]
                i += 1
            else:
                couverture += couverture + 1
                patchs += 1
        return patchs

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minPatches([1, 3], 6) == 1
    assert solution.minPatches([1, 5, 10], 20) == 2
    assert solution.minPatches([1, 2, 2], 5) == 0
    assert solution.minPatches([1, 2, 31, 33], 2147483647) == 28
    print("All tests passed.")
