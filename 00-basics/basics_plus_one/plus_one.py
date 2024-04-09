from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increments the large integer represented by the array `digits` by one.

        Args:
        digits: A list of integers representing the digits of a large integer.

        Returns:
        A list of integers representing the digits of the incremented large integer.
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4], "Test case 1 failed"
    assert solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2], "Test case 2 failed"
    assert solution.plusOne([9]) == [1, 0], "Test case 3 failed"
    assert solution.plusOne([9, 9, 9]) == [1, 0, 0, 0], "Test case 4 failed"