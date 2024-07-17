from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
        Deletes specified nodes from the tree and returns the forest of remaining trees.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.
            to_delete (List[int]): The list of node values to delete.

        Returns:
            List[TreeNode]: The roots of the trees in the remaining forest.
        """
        à_supprimer = set(to_delete)
        forêt = []

        def dfs(nœud, est_parent):
            if not nœud:
                return None
            à_supprimer_nœud = nœud.val in à_supprimer
            if not à_supprimer_nœud and est_parent:
                forêt.append(nœud)
            nœud.left = dfs(nœud.left, à_supprimer_nœud)
            nœud.right = dfs(nœud.right, à_supprimer_nœud)
            return None if à_supprimer_nœud else nœud

        dfs(root, True)
        return forêt


# Test cases
if __name__ == "__main__":
    solution = Solution()


    def build_tree(nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while queue and i < len(nodes):
            current = queue.pop(0)
            if nodes[i] is not None:
                current.left = TreeNode(nodes[i])
                queue.append(current.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                current.right = TreeNode(nodes[i])
                queue.append(current.right)
            i += 1
        return root


    def extract_values(root):
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            node = queue.pop(0)
            result.append(node.val if node else None)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        while result and result[-1] is None:
            result.pop()
        return result


    root1 = build_tree([1, 2, 3, 4, 5, 6, 7])
    assert [extract_values(tree) for tree in solution.delNodes(root1, [3, 5])] == [[1, 2, None, 4], [6], [7]]

    root2 = build_tree([1, 2, 4, None, 3])
    assert [extract_values(tree) for tree in solution.delNodes(root2, [3])] == [[1, 2, 4]]

    print("All tests passed.")
