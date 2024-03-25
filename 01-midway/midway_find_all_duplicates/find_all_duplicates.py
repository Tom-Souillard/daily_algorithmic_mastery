class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Finds all elements in the given array that appear exactly twice.

        This function operates in O(n) time complexity with O(1) extra space, using the input array itself
        to track duplicates by marking visited elements. Elements in the array are in the range [1, n],
        allowing us to use array indices as direct references to the elements' values.

        Args:
        nums: A list of integers where each integer is in the range [1, n] and appears once or twice.

        Returns:
        A list of integers that appear exactly twice in the input array.
        """
        doublons = []
        for nombre in nums:
            index = abs(nombre) - 1
            if nums[index] < 0:
                doublons.append(abs(nombre))
            else:
                nums[index] = -nums[index]
        return doublons
