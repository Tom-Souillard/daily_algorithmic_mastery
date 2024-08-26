from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        Perform a postorder traversal of an n-ary tree and return the values of the nodes.

        Args:
            root (Node): The root node of the n-ary tree.

        Returns:
            List[int]: A list of integers representing the postorder traversal.
        """
        def parcours(node: 'Node') -> List[int]:
            resultat = []
            for enfant in node.children:
                resultat.extend(parcours(enfant))
            resultat.append(node.val)
            return resultat

        return parcours(root) if root else []

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.postorder(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])) == [5, 6, 3, 2, 4, 1]
    assert solution.postorder(Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])) == [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
    print("All tests passed.")
