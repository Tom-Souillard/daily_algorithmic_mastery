class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        """
        This function returns the minimum number of moves required to make all elements in the array unique.

        Args:
            nums: List of integers where each integer can be incremented.

        Returns:
            The minimum number of increments needed to make each element in the array unique.
        """
        nums.sort()
        deplacement_total = 0
        valeur_suivante = nums[0]

        for nombre in nums:
            if nombre < valeur_suivante:
                deplacement_total += valeur_suivante - nombre
                valeur_suivante += 1
            else:
                valeur_suivante = nombre + 1

        return deplacement_total


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minIncrementForUnique([1, 2, 2]) == 1
    assert solution.minIncrementForUnique([3, 2, 1, 2, 1, 7]) == 6
    print("All tests passed.")
