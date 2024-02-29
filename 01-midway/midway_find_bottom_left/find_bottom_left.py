class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        Finds the leftmost value in the last row of a binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            The value of the leftmost node in the last row of the tree.

        This function implements a level-order traversal using a queue, ensuring
        O(n) time complexity where n is the number of nodes in the tree, and
        O(m) space complexity where m is the maximum number of nodes at any level
        in the tree. The first node of the last level encountered during the
        traversal is returned.
        """
        queue = [root]
        while queue:
            tailleActuelle = len(queue)
            for i in range(tailleActuelle):
                noeudActuel = queue.pop(0)
                if i == 0: # first node of the current level
                    valeurGauche = noeudActuel.val
                if noeudActuel.left:
                    queue.append(noeudActuel.left)
                if noeudActuel.right:
                    queue.append(noeudActuel.right)
        return valeurGauche
