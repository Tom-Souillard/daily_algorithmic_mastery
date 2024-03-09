class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Finds the minimum common value between two sorted lists.

        Args:
        nums1: A list of integers sorted in non-decreasing order.
        nums2: Another list of integers sorted in non-decreasing order.

        Returns:
        The smallest integer common to both nums1 and nums2. If there is no common integer, returns -1.

        The approach uses two pointers to traverse both lists efficiently, ensuring that the time complexity is O(n + m) and the space complexity is O(1), where n and m are the lengths of nums1 and nums2, respectively.
        """
        indice1, indice2 = 0, 0
        while indice1 < len(nums1) and indice2 < len(nums2):
            if nums1[indice1] == nums2[indice2]:
                return nums1[indice1]
            elif nums1[indice1] < nums2[indice2]:
                indice1 += 1
            else:
                indice2 += 1
        return -1
