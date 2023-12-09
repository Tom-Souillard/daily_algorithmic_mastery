# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(noeud):
            if not noeud:
                return 0, 0
            excédent_gauche, déplacements_gauche = dfs(noeud.left)
            excédent_droite, déplacements_droite = dfs(noeud.right)
            excédent_actuel = noeud.val + excédent_gauche + excédent_droite - 1
            déplacements_totaux = abs(excédent_actuel) + déplacements_gauche + déplacements_droite
            return excédent_actuel, déplacements_totaux

        return dfs(root)[1]

# Test cases
def test_solution():
    sol = Solution()

    root1 = TreeNode(3)
    root1.left = TreeNode(0)
    root1.right = TreeNode(0)
    assert sol.distributeCoins(root1) == 2

    root2 = TreeNode(0)
    root2.left = TreeNode(3)
    root2.right = TreeNode(0)
    assert sol.distributeCoins(root2) == 3

    root3 = TreeNode(1)
    root3.left = TreeNode(0)
    root3.right = TreeNode(2)
    assert sol.distributeCoins(root3) == 2

    root4 = TreeNode(1)
    root4.left = TreeNode(0)
    root4.right = TreeNode(0)
    root4.right.right = TreeNode(3)
    assert sol.distributeCoins(root4) == 4

test_solution()
