from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums sorted in non-decreasing order, this function
        returns an array of the squares of each number sorted in non-decreasing order.

        The function uses a two-pointer approach to efficiently generate the squared
        and sorted array without needing an explicit sort after squaring the elements,
        optimizing both time and space complexity.

        Args:
        nums: A list of integers sorted in non-decreasing order.

        Returns:
        A list of integers representing the squares of each element in nums, sorted in non-decreasing order.
        """
        gauche, droite = 0, len(nums) - 1
        resultat = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[gauche]) > abs(nums[droite]):
                resultat[i] = nums[gauche] ** 2
                gauche += 1
            else:
                resultat[i] = nums[droite] ** 2
                droite -= 1
        return resultat
