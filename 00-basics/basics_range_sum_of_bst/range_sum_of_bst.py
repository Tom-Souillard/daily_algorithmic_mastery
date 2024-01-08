class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, racine: Optional[TreeNode], bas: int, haut: int) -> int:
        """
        Calculate the sum of values of all nodes with a value in the inclusive range [low, high] in a binary search tree.

        Args:
        racine (Optional[TreeNode]): The root node of the binary search tree.
        bas (int): The lower bound of the range.
        haut (int): The upper bound of the range.

        Returns:
        int: The sum of values of all nodes within the range.
        """
        if not racine:
            return 0

        somme = 0
        if bas <= racine.val <= haut:
            somme += racine.val

        if bas < racine.val:
            somme += self.rangeSumBST(racine.left, bas, haut)
        if racine.val < haut:
            somme += self.rangeSumBST(racine.right, bas, haut)

        return somme
