from typing import Optional

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        Evaluate the boolean value of a full binary tree.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            bool: The boolean value of the binary tree evaluation.
        """
        if not root.left and not root.right:
            return bool(root.val)
        gauche = self.evaluateTree(root.left)
        droit = self.evaluateTree(root.right)
        if root.val == 2:
            return gauche or droit
        else:
            return gauche and droit

# Test cases
def test():
    def create_tree(nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while i < len(nodes):
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

    root1 = create_tree([2,1,3,None,None,0,1])
    assert Solution().evaluateTree(root1) == True
    root2 = create_tree([0])
    assert Solution().evaluateTree(root2) == False
    root3 = create_tree([2,3,1,1,0,None,None,1,0])
    assert Solution().evaluateTree(root3) == True

test()
