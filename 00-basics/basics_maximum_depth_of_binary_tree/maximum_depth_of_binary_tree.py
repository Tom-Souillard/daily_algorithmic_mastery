from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, racine: Optional[TreeNode]) -> int:
        """
        Calculate the maximum depth of a binary tree.

        Args:
        racine (Optional[TreeNode]): The root of the binary tree.

        Returns:
        int: The maximum depth of the tree.
        """
        if not racine:
            return 0
        else:
            profondeur_gauche = self.maxDepth(racine.left)
            profondeur_droite = self.maxDepth(racine.right)
            return max(profondeur_gauche, profondeur_droite) + 1

# Test cases
if __name__ == "__main__":
    # Helper function to create a binary tree from list input
    def insert_level_order(arr, root, i, n):
        if i < n:
            temp = TreeNode(arr[i])
            root = temp
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
        return root

    arr1 = [3, 9, 20, None, None, 15, 7]
    n1 = len(arr1)
    root1 = None
    root1 = insert_level_order(arr1, root1, 0, n1)
    solution = Solution()
    print("Expected: 3", "Got:", solution.maxDepth(root1))

    arr2 = [1, None, 2]
    n2 = len(arr2)
    root2 = None
    root2 = insert_level_order(arr2, root2, 0, n2)
    print("Expected: 2", "Got:", solution.maxDepth(root2))
