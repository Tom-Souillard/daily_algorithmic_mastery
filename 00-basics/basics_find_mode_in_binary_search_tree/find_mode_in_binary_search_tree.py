from typing import List, Optional
# Définition de la classe TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        Find and return the mode(s) in a Binary Search Tree (BST).

        Given the root of a BST with duplicates, this function returns all the
        mode(s) i.e., the most frequently occurring element(s).

        Args:
            root (Optional[TreeNode]): The root node of the BST. Can be `None`.

        Returns:
            List[int]: A list containing the mode(s) of the BST. If the tree has
            more than one mode, they are returned in any order.
        """

        def dfs(node, prev_val, count, max_count, modes):
            if not node:
                return prev_val, count, max_count

            prev_val, count, max_count = dfs(node.left, prev_val, count, max_count, modes)

            if prev_val is not None and node.val == prev_val:
                count += 1
            else:
                count = 1

            if count > max_count:
                max_count = count
                modes.clear()

            if count == max_count:
                modes.append(node.val)

            return dfs(node.right, node.val, count, max_count, modes)

        modes = []
        dfs(root, None, 0, 0, modes)
        return modes

# Fonction pour construire un arbre à partir d'une liste (utilisé pour les tests)
def build_tree(lst, index):
    if index >= len(lst) or lst[index] is None:
        return None
    node = TreeNode(lst[index])
    node.left = build_tree(lst, 2 * index + 1)
    node.right = build_tree(lst, 2 * index + 2)
    return node

# Exécution des tests
if __name__ == "__main__":
    sol = Solution()

    # Test 1
    root1 = build_tree([1, None, 2, 2], 0)
    answer1 = [2]
    print("Test 1: ", sol.findMode(root1) == answer1)  # Devrait afficher [2]

    # Test 2
    root2 = build_tree([0], 0)
    answer2 = [0]
    print("Test 2: ", sol.findMode(root2) == answer2)  # Devrait afficher [0]