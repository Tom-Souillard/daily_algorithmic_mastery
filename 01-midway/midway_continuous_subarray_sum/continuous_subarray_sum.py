class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
        Checks if the array has a subarray of at least two elements whose sum is a multiple of k.

        Args:
            nums (list[int]): The input array of integers.
            k (int): The integer to check multiples against.

        Returns:
            bool: True if such a subarray exists, False otherwise.
        """
        prefix_sum = 0
        mod_dict = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k

            if mod in mod_dict:
                if i - mod_dict[mod] > 1:
                    return True
            else:
                mod_dict[mod] = i

        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.checkSubarraySum([23, 2, 4, 6, 7], 6) == True
    assert solution.checkSubarraySum([23, 2, 6, 4, 7], 6) == True
    assert solution.checkSubarraySum([23, 2, 6, 4, 7], 13) == False
    assert solution.checkSubarraySum([5, 0, 0, 0], 3) == True
    assert solution.checkSubarraySum([0, 1, 0], 2) == False
    print("All tests passed.")
