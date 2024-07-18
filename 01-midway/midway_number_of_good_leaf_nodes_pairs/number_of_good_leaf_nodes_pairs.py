# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        Count the number of good leaf node pairs within a given distance in a binary tree.

        Args:
            root (TreeNode): The root of the binary tree.
            distance (int): The maximum distance between good leaf node pairs.

        Returns:
            int: The number of good leaf node pairs.
        """

        def dfs(node: TreeNode) -> list:
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.good_pairs += 1
            return [n + 1 for n in left_distances + right_distances if n + 1 < distance]

        self.good_pairs = 0
        dfs(root)
        return self.good_pairs


# Test cases
if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(4)
    assert solution.countPairs(root1, 3) == 1

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)
    assert solution.countPairs(root2, 3) == 2

    root3 = TreeNode(7)
    root3.left = TreeNode(1)
    root3.right = TreeNode(4)
    root3.left.left = TreeNode(6)
    root3.right.left = TreeNode(5)
    root3.right.right = TreeNode(3)
    root3.right.right.left = TreeNode(2)
    assert solution.countPairs(root3, 3) == 1

    print("All tests passed.")
