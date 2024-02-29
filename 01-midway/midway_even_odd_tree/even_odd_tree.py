class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """
        Checks if a binary tree is an Even-Odd tree. A binary tree is Even-Odd if
        for every even-indexed level, all nodes have odd integer values in strictly
        increasing order, and for every odd-indexed level, all nodes have even integer
        values in strictly decreasing order.

        Args:
        root: TreeNode - The root node of the binary tree.

        Returns:
        bool: True if the binary tree is Even-Odd, otherwise False.
        """
        if not root:
            return False

        niveau = 0
        queue = [root]

        while queue:
            niveau_taille = len(queue)
            prev_val = float('-inf') if niveau % 2 == 0 else float('inf')
            for _ in range(niveau_taille):
                noeud = queue.pop(0)
                if niveau % 2 == 0:  # Even level: values must be odd and strictly increasing.
                    if noeud.val % 2 == 0 or noeud.val <= prev_val:
                        return False
                else:  # Odd level: values must be even and strictly decreasing.
                    if noeud.val % 2 != 0 or noeud.val >= prev_val:
                        return False
                prev_val = noeud.val

                if noeud.left:
                    queue.append(noeud.left)
                if noeud.right:
                    queue.append(noeud.right)
            niveau += 1

        return True
