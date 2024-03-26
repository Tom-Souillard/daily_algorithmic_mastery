class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Finds the smallest positive integer that is missing from the array.

        This function modifies the input array `nums` in-place to use indices as a way to mark the presence of integers. It ensures that only positive integers within the valid range are considered during the marking process. The function then scans the modified array to identify the smallest missing positive integer by looking for the first index that does not follow the marking convention.

        Args:
        nums (List[int]): An unsorted list of integers.

        Returns:
        int: The smallest positive integer that is not in `nums`.
        """
        taille = len(nums)
        for i in range(taille):
            # Mark nums[i] as negative if i+1 is found in nums
            while 1 <= nums[i] <= taille and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Find the first cell which does not contain i+1
        for i in range(taille):
            if nums[i] != i + 1:
                return i + 1

        # If the nums array forms a sequence from 1 to n
        return taille + 1
