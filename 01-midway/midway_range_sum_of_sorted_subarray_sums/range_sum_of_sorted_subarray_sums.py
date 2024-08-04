from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
        Computes the sum of the numbers from index `left` to `right` (indexed from 1),
        inclusive, in the sorted list of all non-empty continuous subarray sums.

        Args:
        nums (List[int]): List of positive integers.
        n (int): Length of the list `nums`.
        left (int): Start index (1-based) for the sum range.
        right (int): End index (1-based) for the sum range.

        Returns:
        int: The sum of the numbers in the specified range modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7
        sous_totaux = []

        for i in range(n):
            somme = 0
            for j in range(i, n):
                somme += nums[j]
                sous_totaux.append(somme)

        sous_totaux.sort()
        return sum(sous_totaux[left - 1:right]) % MOD


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.rangeSum([1, 2, 3, 4], 4, 1, 5) == 13
    assert solution.rangeSum([1, 2, 3, 4], 4, 3, 4) == 6
    assert solution.rangeSum([1, 2, 3, 4], 4, 1, 10) == 50
    print("All tests passed.")
