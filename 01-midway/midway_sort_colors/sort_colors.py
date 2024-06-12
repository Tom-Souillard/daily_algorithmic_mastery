class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Sort an array with elements 0, 1, and 2 in-place.

        Args:
            nums (list[int]): List of integers where each integer is 0, 1, or 2.

        Returns:
            None
        """
        rouge, blanc, bleu = 0, 0, len(nums) - 1
        while blanc <= bleu:
            if nums[blanc] == 0:
                nums[rouge], nums[blanc] = nums[blanc], nums[rouge]
                rouge += 1
                blanc += 1
            elif nums[blanc] == 1:
                blanc += 1
            else:
                nums[blanc], nums[bleu] = nums[bleu], nums[blanc]
                bleu -= 1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.sortColors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
    assert solution.sortColors([2, 0, 1]) == [0, 1, 2]
    assert solution.sortColors([1, 2, 0]) == [0, 1, 2]
    assert solution.sortColors([1, 0, 1, 2, 0, 1, 2, 1, 0]) == [0, 0, 0, 1, 1, 1, 1, 2, 2]
    print("All tests passed.")
