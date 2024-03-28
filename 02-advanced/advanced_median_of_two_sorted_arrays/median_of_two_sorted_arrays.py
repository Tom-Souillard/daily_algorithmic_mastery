class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays efficiently.

        This function aims to find the median of two sorted arrays with minimum time complexity.
        It uses binary search in the shorter array to ensure the median is found in O(log(min(m,n))) time,
        where m and n are the lengths of the two input arrays.

        Args:
            nums1: A list of integers representing the first sorted array.
            nums2: A list of integers representing the second sorted array.

        Returns:
            A float value representing the median of the two sorted arrays.
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        longueur1, longueur2 = len(nums1), len(nums2)
        debut, fin = 0, longueur1
        while debut <= fin:
            positionX = (debut + fin) // 2
            positionY = (longueur1 + longueur2 + 1) // 2 - positionX

            maxGaucheX = float('-infinity') if positionX == 0 else nums1[positionX - 1]
            minDroiteX = float('infinity') if positionX == longueur1 else nums1[positionX]

            maxGaucheY = float('-infinity') if positionY == 0 else nums2[positionY - 1]
            minDroiteY = float('infinity') if positionY == longueur2 else nums2[positionY]

            if maxGaucheX <= minDroiteY and maxGaucheY <= minDroiteX:
                if (longueur1 + longueur2) % 2 == 0:
                    return (max(maxGaucheX, maxGaucheY) + min(minDroiteX, minDroiteY)) / 2
                else:
                    return max(maxGaucheX, maxGaucheY)
            elif maxGaucheX > minDroiteY:
                fin = positionX - 1
            else:
                debut = positionX + 1

        raise ValueError("Les tableaux doivent être triés et non vides.")
