from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        Find the shortest path from start node to destination node in a binary tree.

        Args:
            root (TreeNode): The root of the binary tree.
            startValue (int): The value of the start node.
            destValue (int): The value of the destination node.

        Returns:
            str: The directions from the start node to the destination node using 'L', 'R', 'U'.
        """

        def trouver_chemin(racine: Optional[TreeNode], valeur: int) -> Optional[str]:
            if not racine:
                return None
            if racine.val == valeur:
                return ""
            gauche = trouver_chemin(racine.left, valeur)
            if gauche is not None:
                return "L" + gauche
            droite = trouver_chemin(racine.right, valeur)
            if droite is not None:
                return "R" + droite
            return None

        chemin_depart = trouver_chemin(root, startValue)
        chemin_destination = trouver_chemin(root, destValue)

        i = 0
        while i < len(chemin_depart) and i < len(chemin_destination) and chemin_depart[i] == chemin_destination[i]:
            i += 1

        chemin_depart = chemin_depart[i:]
        chemin_destination = chemin_destination[i:]

        return "U" * len(chemin_depart) + chemin_destination


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.getDirections(TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4))), 3,
                                  6) == "UURL"
    assert solution.getDirections(TreeNode(2, TreeNode(1)), 2, 1) == "L"
    print("All tests passed.")
