from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        Args:
            nums: A list of integers representing the array of numbers.
            k: An integer representing the k-th position.

        Returns:
            The k-th smallest distance between pairs of integers in the array.
        """
        nums.sort()
        gauche, droite = 0, nums[-1] - nums[0]

        def count_pairs(distance: int) -> int:
            count, j = 0, 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= distance:
                    j += 1
                count += j - i - 1
            return count

        while gauche < droite:
            milieu = (gauche + droite) // 2
            if count_pairs(milieu) < k:
                gauche = milieu + 1
            else:
                droite = milieu

        return gauche


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.smallestDistancePair([1, 3, 1], 1) == 0
    assert solution.smallestDistancePair([1, 1, 1], 2) == 0
    assert solution.smallestDistancePair([1, 6, 1], 3) == 5
    print("All tests passed.")
