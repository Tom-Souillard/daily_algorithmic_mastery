class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of val in nums in-place, returns the new length.

        This method modifies nums such that the first k elements contain all the elements
        not equal to val. The order of elements can be changed. It aims for minimal space
        and time complexity.

        Args:
            nums: List[int]. The list of numbers to process.
            val: int. The value to remove from nums.

        Returns:
            int. The length of nums after removing all instances of val.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
