from collections import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        """
        Sorts an array in increasing order basing on the frequency of the values. If multiple values have the same frequency, sorts them in decreasing order.

        Args:
            nums(list[int]): List of integer to be sorted.

        Returns:
            list[int]: Sorted list of integers.
        """
        frequence = Counter(nums)
        return sorted(nums, key=lambda x: (frequence[x], -x))


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.frequencySort([1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]
    assert solution.frequencySort([2, 3, 1, 3, 2]) == [1, 3, 3, 2, 2]
    assert solution.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]) == [5, -1, 4, 4, -6, -6, 1, 1, 1]
    print("All tests passed.")

# from collections import Counter
#
# def demo(input):
#     freq = Counter(input)
#     lst = list(freq.items())
#     new_lst = sorted(lst, key= lambda x: x[1])
#     result = []
#     for i in new_lst:
#         result.extend([i[0]] * i[1])
#     return result