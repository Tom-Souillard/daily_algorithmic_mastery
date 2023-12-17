from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array.

        Args:
            nums (List[int]): The input array, which is a rotated sorted array.
            target (int): The target value to search for in the array.

        Returns:
            int: The index of the target in the array if present, otherwise -1.
        """
        debut, fin = 0, len(nums) - 1
        while debut <= fin:
            milieu = (debut + fin) // 2
            if nums[milieu] == target:
                return milieu
            if nums[debut] <= nums[milieu]:
                if nums[debut] <= target < nums[milieu]:
                    fin = milieu - 1
                else:
                    debut = milieu + 1
            else:
                if nums[milieu] < target <= nums[fin]:
                    debut = milieu + 1
                else:
                    fin = milieu - 1
        return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4, "Test case 1 failed"
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1, "Test case 2 failed"
    assert solution.search([1], 0) == -1, "Test case 3 failed"
    assert solution.search([5, 1, 3], 3) == 2, "Test case 4 failed"
