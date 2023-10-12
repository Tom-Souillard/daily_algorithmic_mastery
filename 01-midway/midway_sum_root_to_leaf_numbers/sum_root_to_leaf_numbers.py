from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        This method calculates the total sum of all root-to-leaf numbers represented by the paths in a binary tree.
        Each path forms a number by concatenating the values from root to leaf.

        Args:
        root (Optional[TreeNode]): The root of the binary tree containing digits from 0 to 9 only.

        Returns:
        int: The total sum of all the numbers formed by root-to-leaf paths.
        """

        def sommeNumeros(noeud, somme_courante):
            if not noeud:
                return 0
            somme_courante = somme_courante * 10 + noeud.val
            if not noeud.left and not noeud.right:
                return somme_courante
            return sommeNumeros(noeud.left, somme_courante) + sommeNumeros(noeud.right, somme_courante)

        return sommeNumeros(root, 0)


# Test cases
if __name__ == "__main__":
    # Define the tree nodes
    n1 = TreeNode(4)
    n2 = TreeNode(9)
    n3 = TreeNode(0)
    n4 = TreeNode(5)
    n5 = TreeNode(1)

    # Connect nodes
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    solution = Solution()
    print(solution.sumNumbers(n1))  # Output: 1026
