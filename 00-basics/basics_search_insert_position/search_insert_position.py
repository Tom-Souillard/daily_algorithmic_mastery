from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Finds the index of the target value in a sorted array of distinct integers. If the target is not found, returns the index where it would be if it were inserted in order.

        Args:
        nums: A list of integers in ascending order.
        target: The integer to find or insert.

        Returns:
        The index of the target if found, or the index where the target should be inserted.
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    assert solution.searchInsert([1,3,5,6], 5) == 2, "Test 1"
    assert solution.searchInsert([1,3,5,6], 2) == 1, "Test 2"
    assert solution.searchInsert([1,3,5,6], 7) == 4, "Test 3"
    print("test ok")