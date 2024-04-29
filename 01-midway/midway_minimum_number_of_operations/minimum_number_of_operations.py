from typing import List
from functools import reduce
from operator import xor

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Calculate the minimum number of bit flips required to make the XOR of all array elements equal to k.

        Args:
        nums (List[int]): List of integers.
        k (int): Target XOR value.

        Returns:
        int: Minimum number of bit flips required.
        """
        return (reduce(xor, nums) ^ k).bit_count()

# Test cases 
if __name__ == "__main__":
    solution = Solution()
    assert solution.minOperations([2, 1, 3, 4], 1) == 2
    assert solution.minOperations([2, 0, 2, 0], 0) == 0
