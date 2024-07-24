from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """
        Sort the array based on the mapped values of its elements.

        Args:
        mapping (List[int]): The mapping rule of a shuffled decimal system.
        nums (List[int]): The array of integers to be sorted.

        Returns:
        List[int]: The sorted array based on the mapped values.
        """

        def map_value(n: int) -> int:
            mapped_str = ''.join(str(mapping[int(digit)]) for digit in str(n))
            return int(mapped_str.lstrip('0') or '0')

        return sorted(nums, key=map_value)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.sortJumbled([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]) == [338, 38, 991]
    assert solution.sortJumbled([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [789, 456, 123]) == [123, 456, 789]
    assert solution.sortJumbled([1, 0, 3, 2, 5, 4, 7, 6, 9, 8], [10, 20, 30]) == [10, 30, 20]
    assert solution.sortJumbled([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [321, 654, 987]) == [987, 654, 321]
    print("All tests passed.")
