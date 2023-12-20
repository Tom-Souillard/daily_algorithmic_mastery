from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the starting and ending position of a given target value in a sorted array.

        Args:
        nums: List of integers sorted in non-decreasing order.
        target: The target value to find in nums.

        Returns:
        A list containing the starting and ending positions of the target value. If the target is not found, returns [-1, -1].
        """

        def trouverDebutFin(nums, target, trouverDebut):
            position = -1
            debut, fin = 0, len(nums) - 1
            while debut <= fin:
                milieu = (debut + fin) // 2
                if nums[milieu] > target:
                    fin = milieu - 1
                elif nums[milieu] < target:
                    debut = milieu + 1
                else:
                    position = milieu
                    if trouverDebut:
                        fin = milieu - 1
                    else:
                        debut = milieu + 1
            return position

        debut = trouverDebutFin(nums, target, True)
        fin = trouverDebutFin(nums, target, False)
        return [debut, fin]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))  # Expected: [3,4]
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))  # Expected: [-1,-1]
    print(solution.searchRange([], 0))  # Expected: [-1,-1]
    # Additional test cases
    print(solution.searchRange([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))  # Expected: [4,4]
    print(solution.searchRange([2, 2, 2, 3, 3, 3, 4, 4, 4], 3))  # Expected: [3,5]
