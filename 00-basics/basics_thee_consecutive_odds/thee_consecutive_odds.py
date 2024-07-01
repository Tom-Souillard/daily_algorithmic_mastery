class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        """
        Determine if there are three consecutive odd numbers in the array.

        Args:
            arr (list[int]): The input list of integers.

        Returns:
            bool: True if there are three consecutive odd numbers, otherwise False.
        """
        compte = 0
        for nombre in arr:
            if nombre % 2 != 0:
                compte += 1
                if compte == 3:
                    return True
            else:
                compte = 0
        return False

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.threeConsecutiveOdds([2, 6, 4, 1]) == False
    assert solution.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]) == True
    assert solution.threeConsecutiveOdds([1, 3, 5, 7, 9]) == True
    assert solution.threeConsecutiveOdds([2, 4, 6, 8, 10]) == False
    assert solution.threeConsecutiveOdds([1, 3, 5, 2, 3, 5, 7]) == True
    print("All tests passed.")
