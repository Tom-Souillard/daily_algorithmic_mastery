from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        Given the root of a binary tree, returns an array of the largest value in each row of the tree (0-indexed).

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: A list containing the largest values for each row in the tree.
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_max = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                level_max = max(level_max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_max)

        return result
