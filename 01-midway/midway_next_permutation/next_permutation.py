class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Finds the next lexicographically greater permutation of the given integer array.

        Args:
            nums (List[int]): The input array of integers.

        Modifies the input array to its next permutation in-place. If no such permutation exists
        (i.e., the array is sorted in descending order), it rearranges the array into its lowest
        possible order (ascending order).
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        debut, fin = i + 1, len(nums) - 1
        while debut < fin:
            nums[debut], nums[fin] = nums[fin], nums[debut]
            debut, fin = debut + 1, fin - 1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3]
    solution.nextPermutation(nums1)
    assert nums1 == [1, 3, 2], f"Expected [1, 3, 2], got {nums1}"

    nums2 = [3, 2, 1]
    solution.nextPermutation(nums2)
    assert nums2 == [1, 2, 3], f"Expected [1, 2, 3], got {nums2}"

    nums3 = [1, 1, 5]
    solution.nextPermutation(nums3)
    assert nums3 == [1, 5, 1], f"Expected [1, 5, 1], got {nums3}"

    nums4 = [1, 5, 1]
    solution.nextPermutation(nums4)
    assert nums4 == [5, 1, 1], f"Expected [5, 1, 1], got {nums4}"
