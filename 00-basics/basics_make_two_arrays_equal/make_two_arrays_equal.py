from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        """
        Determine if two arrays can be made equal by reversing any subarrays.

        Args:
            target (List[int]): The target array.
            arr (List[int]): The array to be transformed.

        Returns:
            bool: True if arr can be transformed to match target, False otherwise.
        """
        return sorted(target) == sorted(arr)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]) == True
    assert solution.canBeEqual([7], [7]) == True
    assert solution.canBeEqual([3, 7, 9], [3, 7, 11]) == False
    assert solution.canBeEqual([1, 1, 1, 1], [1, 1, 1, 1]) == True
    assert solution.canBeEqual([1, 2, 3], [3, 2, 1]) == True
    print("All tests passed.")
