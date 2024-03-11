class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Finds the intersection of two integer arrays.

        Args:
        nums1: A list of integers representing the first array.
        nums2: A list of integers representing the second array.

        Returns:
        A list containing the unique elements found in both nums1 and nums2. The elements in the result can be in any order.
        """
        ensemble1 = set(nums1)
        ensemble2 = set(nums2)
        return list(ensemble1 & ensemble2)
