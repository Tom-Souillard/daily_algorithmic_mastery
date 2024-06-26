from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        Balance a binary search tree.

        Args:
            root (TreeNode): The root of the binary search tree.

        Returns:
            TreeNode: The root of the balanced binary search tree.
        """

        def inorder_traversal(noeud: Optional[TreeNode]) -> List[int]:
            return inorder_traversal(noeud.left) + [noeud.val] + inorder_traversal(noeud.right) if noeud else []

        def build_balanced_bst(elements: List[int]) -> Optional[TreeNode]:
            if not elements:
                return None
            milieu = len(elements) // 2
            racine = TreeNode(elements[milieu])
            racine.left = build_balanced_bst(elements[:milieu])
            racine.right = build_balanced_bst(elements[milieu + 1:])
            return racine

        elements = inorder_traversal(root)
        return build_balanced_bst(elements)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root1 = TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4))))
    assert solution.balanceBST(root1).val in [2, 3]

    # Test case 2
    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    assert solution.balanceBST(root2).val == 2

    print("All tests passed.")