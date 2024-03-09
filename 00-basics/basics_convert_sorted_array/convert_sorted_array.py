from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """Converts a sorted array into a height-balanced binary search tree.

        Args:
            nums: A list of integers sorted in ascending order.

        Returns:
            A TreeNode representing the root of the height-balanced binary search tree.
        """

        def creerArbre(gauche, droite):
            if gauche > droite:
                return None
            milieu = (gauche + droite) // 2
            racine = TreeNode(nums[milieu])
            racine.left = creerArbre(gauche, milieu - 1)
            racine.right = creerArbre(milieu + 1, droite)
            return racine

        return creerArbre(0, len(nums) - 1)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    test_nums1 = [-10, -3, 0, 5, 9]
    bst1 = solution.sortedArrayToBST(test_nums1)

    test_nums2 = [1, 3]
    bst2 = solution.sortedArrayToBST(test_nums2)

    test_nums3 = [1, 2, 3, 4, 5, 6, 7]
    bst3 = solution.sortedArrayToBST(test_nums3)
