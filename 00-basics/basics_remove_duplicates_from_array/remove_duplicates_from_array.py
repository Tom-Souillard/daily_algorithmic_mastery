class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place, returning the number of unique elements.
        Minimizes assignments in the array for optimized performance.

        Args:
        nums (List[int]): Sorted integer array from which duplicates are to be removed.

        Returns:
        int: The number of unique elements after removing duplicates.
        """
        if not nums:
            return 0

        indiceUnique = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[indiceUnique]:
                indiceUnique += 1
                if i != indiceUnique:
                    nums[indiceUnique] = nums[i]

        return indiceUnique + 1

# Example usage:
sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))  # Output: 5
print(nums)  # Output: [0, 1, 2, 3, 4, _, _, _, _, _]
