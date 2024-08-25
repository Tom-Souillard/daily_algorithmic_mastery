# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the postorder traversal of the nodes' values in a binary tree.

        Args:
            root (TreeNode): The root of the binary tree.

        Returns:
            List[int]: The postorder traversal of the binary tree.
        """
        if not root:
            return []
        result = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            result.append(node.val)

        traverse(root)
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [3, 2, 1]
    assert solution.postorderTraversal(None) == []
    assert solution.postorderTraversal(TreeNode(1)) == [1]
    assert solution.postorderTraversal(TreeNode(1, TreeNode(2), TreeNode(3))) == [2, 3, 1]
    assert solution.postorderTraversal(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))) == [3, 2, 4, 1]
    print("All tests passed.")
