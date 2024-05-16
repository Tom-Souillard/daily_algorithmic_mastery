from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        Remove all the leaf nodes with the given target value from the binary tree.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.
            target (int): The target value for leaf nodes to be deleted.

        Returns:
            Optional[TreeNode]: The root of the binary tree after deleting the target leaf nodes.
        """
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root


# Test cases
def test_removeLeafNodes():
    solution = Solution()

    def build_tree(nodes):
        if not nodes:
            return None
        val = nodes.pop(0)
        if val is None:
            return None
        root = TreeNode(val)
        queue = [root]
        while nodes:
            node = queue.pop(0)
            left_val = nodes.pop(0) if nodes else None
            right_val = nodes.pop(0) if nodes else None
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
        return root

    def tree_to_list(root):
        if not root:
            return []
        result = []
        queue = [root]
        while any(queue):
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left if node else None)
                queue.append(node.right if node else None)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

    root1 = build_tree([1, 2, 3, 2, None, 2, 4])
    target1 = 2
    expected1 = [1, None, 3, None, 4]
    result1 = solution.removeLeafNodes(root1, target1)
    assert tree_to_list(result1) == expected1

    root2 = build_tree([1, 3, 3, 3, 2])
    target2 = 3
    expected2 = [1, 3, None, None, 2]
    result2 = solution.removeLeafNodes(root2, target2)
    assert tree_to_list(result2) == expected2

    root3 = build_tree([1, 2, None, 2, None, 2])
    target3 = 2
    expected3 = [1]
    result3 = solution.removeLeafNodes(root3, target3)
    assert tree_to_list(result3) == expected3

    root4 = build_tree([1, 1, 1])
    target4 = 1
    expected4 = []
    result4 = solution.removeLeafNodes(root4, target4)
    assert tree_to_list(result4) == expected4

    root5 = build_tree([1])
    target5 = 1
    expected5 = []
    result5 = solution.removeLeafNodes(root5, target5)
    assert tree_to_list(result5) == expected5


test_removeLeafNodes()