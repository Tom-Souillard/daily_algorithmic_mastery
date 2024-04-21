from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Determines if a path exists between a source and a destination vertex in a graph.

        Args:
        n (int): The number of vertices in the graph.
        edges (List[List[int]]): A list of edges where each edge is represented as a list [u, v].
        source (int): The source vertex.
        destination (int): The destination vertex.

        Returns:
        bool: True if a valid path exists from the source to the destination, otherwise False.
        """
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        visite = set([source])

        while queue:
            noeud = queue.popleft()
            if noeud == destination:
                return True
            for voisin in graph[noeud]:
                if voisin not in visite:
                    visite.add(voisin)
                    queue.append(voisin)

        return False


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))  # Output: true
    print(sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))  # Output: false
    print(sol.validPath(4, [[0, 1], [1, 2], [2, 3]], 0, 3))  # Output: true
