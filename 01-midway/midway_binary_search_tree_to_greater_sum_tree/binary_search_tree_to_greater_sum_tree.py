from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        Converts a binary search tree to a greater sum tree where each node's value
        is replaced by the sum of all greater or equal node values in the tree.

        Args:
            root (TreeNode): The root of the binary search tree.

        Returns:
            TreeNode: The root of the greater sum tree.
        """
        somme = 0

        def transformer_arbre(noeud: Optional[TreeNode]):
            nonlocal somme
            if noeud:
                transformer_arbre(noeud.right)
                somme += noeud.val
                noeud.val = somme
                transformer_arbre(noeud.left)

        transformer_arbre(root)
        return root


# Test cases
if __name__ == "__main__":
    solution = Solution()


    def build_tree(nodes, index=0):
        if index < len(nodes) and nodes[index] is not None:
            node = TreeNode(nodes[index])
            node.left = build_tree(nodes, 2 * index + 1)
            node.right = build_tree(nodes, 2 * index + 2)
            return node
        return None


    def tree_to_list(root):
        result = []
        queue = [(root, 0)]
        while queue:
            node, index = queue.pop(0)
            if node:
                while len(result) <= index:
                    result.append(None)
                result[index] = node.val
                queue.append((node.left, 2 * index + 1))
                queue.append((node.right, 2 * index + 2))
        return result


    root1 = build_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    output1 = tree_to_list(solution.bstToGst(root1))
    assert output1 == [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]

    root2 = build_tree([0, None, 1])
    output2 = tree_to_list(solution.bstToGst(root2))
    assert output2 == [1, None, 1]

    print("All tests passed.")

