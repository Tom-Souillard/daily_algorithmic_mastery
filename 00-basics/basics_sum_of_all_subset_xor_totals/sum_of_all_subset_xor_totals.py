from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        Calculate the sum of all subset XOR totals for the given list of integers.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The sum of all subset XOR totals.
        """

        def subsetXOR(sous_ensemble, index):
            if index == len(nums):
                return sous_ensemble
            return subsetXOR(sous_ensemble, index + 1) + subsetXOR(sous_ensemble ^ nums[index], index + 1)

        return subsetXOR(0, 0)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.subsetXORSum([1, 3]))  # Expected output: 6
    print(solution.subsetXORSum([5, 1, 6]))  # Expected output: 28
    print(solution.subsetXORSum([3, 4, 5, 6, 7, 8]))  # Expected output: 480
    print(solution.subsetXORSum([0, 0, 0]))  # Expected output: 0
    print(solution.subsetXORSum([2, 4, 6, 8]))  # Expected output: 64
