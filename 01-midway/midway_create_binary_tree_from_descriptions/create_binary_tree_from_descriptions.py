from typing import List, Optional, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        """
        Constructs a binary tree from a list of descriptions indicating parent-child relationships.

        Args:
            descriptions (List[List[int]]): A list of descriptions where each description is a list of three integers
            representing parent, child, and whether the child is a left child (1) or right child (0).

        Returns:
            Optional[TreeNode]: The root of the constructed binary tree.
        """
        noeuds = {}
        enfants = set()

        for parent, enfant, gauche in descriptions:
            if parent not in noeuds:
                noeuds[parent] = TreeNode(parent)
            if enfant not in noeuds:
                noeuds[enfant] = TreeNode(enfant)

            if gauche:
                noeuds[parent].left = noeuds[enfant]
            else:
                noeuds[parent].right = noeuds[enfant]

            enfants.add(enfant)

        for parent, _, _ in descriptions:
            if parent not in enfants:
                return noeuds[parent]
        return None


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]).val == 50
    assert solution.createBinaryTree([[1, 2, 1], [2, 3, 0], [3, 4, 1]]).val == 1
    print("All tests passed.")
