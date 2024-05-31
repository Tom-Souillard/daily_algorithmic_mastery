from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Find the two elements that appear only once in an array where all other elements appear exactly twice.

        Args:
            nums (List[int]): List of integers with exactly two unique elements and all others occurring twice.

        Returns:
            List[int]: The two unique elements.
        """
        xor_total = 0
        for num in nums:
            xor_total ^= num

        diff_bit = xor_total & -xor_total

        unique1, unique2 = 0, 0
        for num in nums:
            if num & diff_bit:
                unique1 ^= num
            else:
                unique2 ^= num

        return [unique1, unique2]


# Test cases
if __name__ == "__main__":
    assert Solution().singleNumber([1, 2, 1, 3, 2, 5]) in [[3, 5], [5, 3]]
    assert Solution().singleNumber([-1, 0]) in [[-1, 0], [0, -1]]
    assert Solution().singleNumber([0, 1]) in [[1, 0], [0, 1]]
