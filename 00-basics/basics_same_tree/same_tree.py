class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Checks if two binary trees are the same.

        Args:
        p: Optional[TreeNode] - Root of the first binary tree.
        q: Optional[TreeNode] - Root of the second binary tree.

        Returns:
        bool - True if both trees are the same, False otherwise.

        The trees are considered the same if they are structurally identical and the nodes have the same value.
        This function performs a depth-first search (DFS) comparing each node of both trees recursively.
        """

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
