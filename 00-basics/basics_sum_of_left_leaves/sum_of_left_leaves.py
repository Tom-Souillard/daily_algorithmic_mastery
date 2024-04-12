from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the sum of all left leaves in the binary tree.

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        int: The sum of the values of all left leaves.
        """

        def estFeuille(noeud):
            return not noeud.left and not noeud.right

        def aux(noeud, estGauche):
            if not noeud:
                return 0
            if estFeuille(noeud):
                return noeud.val if estGauche else 0
            return aux(noeud.left, True) + aux(noeud.right, False)

        return aux(root, False)


# Test cases
if __name__ == "__main__":
    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5

    solution = Solution()
    print(solution.sumOfLeftLeaves(n1))  # Output should be 24
