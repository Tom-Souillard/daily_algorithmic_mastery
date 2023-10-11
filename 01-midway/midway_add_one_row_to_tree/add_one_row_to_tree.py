from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """Add a row of nodes with specified value at a given depth in the binary tree.

        Args:
        root: TreeNode, the root of the binary tree.
        val: int, value to assign to the new row of nodes.
        depth: int, the depth at which to add the new row of nodes.

        Returns:
        TreeNode, the root of the modified tree.
        """
        if depth == 1:
            return TreeNode(val, root, None)
        queue = [root]
        niveau_actuel = 1
        while queue:
            taille = len(queue)
            if niveau_actuel == depth - 1:
                for _ in range(taille):
                    noeud = queue.pop(0)
                    noeud.left = TreeNode(val, noeud.left, None)
                    noeud.right = TreeNode(val, None, noeud.right)
                return root
            for _ in range(taille):
                noeud = queue.pop(0)
                if noeud.left:
                    queue.append(noeud.left)
                if noeud.right:
                    queue.append(noeud.right)
            niveau_actuel += 1


# Test cases
if __name__ == "__main__":
    # Construction de l'arbre: [4,2,null,3,1]
    racine = TreeNode(4)
    racine.left = TreeNode(2, TreeNode(3), TreeNode(1))

    # Solution
    solution = Solution()
    nouvelle_racine = solution.addOneRow(racine, 1, 3)


    # Fonction pour afficher l'arbre en BFS pour vérifier
    def print_tree(root):
        result = []
        queue = [root]
        while any(queue):
            noeud = queue.pop(0)
            if noeud:
                result.append(noeud.val)
                queue.append(noeud.left)
                queue.append(noeud.right)
            else:
                result.append('null')
        print(result)


    print_tree(nouvelle_racine)  # Doit afficher [4, 2, 'null', 1, 1, 3, 'null', 'null', 1]
