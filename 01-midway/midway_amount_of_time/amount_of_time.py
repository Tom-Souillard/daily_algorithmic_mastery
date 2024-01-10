class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        Calculate the time taken to infect the entire binary tree.

        Args:
        root (Optional[TreeNode]): Root of the binary tree.
        start (int): The value of the node where the infection starts.

        Returns:
        int: The time taken to infect the entire tree.
        """
        # Create a graph from the tree
        graph = {}
        def buildGraph(node, parent=None):
            if node:
                if node.val not in graph:
                    graph[node.val] = []
                if parent:
                    graph[node.val].append(parent)
                    graph[parent].append(node.val)
                buildGraph(node.left, node.val)
                buildGraph(node.right, node.val)

        buildGraph(root)

        # BFS to find the farthest node from the start
        queue = deque([start])
        seen = set([start])
        temps = -1

        while queue:
            for _ in range(len(queue)):
                noeud = queue.popleft()
                for voisin in graph[noeud]:
                    if voisin not in seen:
                        seen.add(voisin)
                        queue.append(voisin)
            temps += 1

        return temps
