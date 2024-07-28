from collections import deque
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        """
        Returns the second minimum time to reach from vertex 1 to vertex n.

        Args:
            n (int): Number of vertices.
            edges (List[List[int]]): Edges in the graph.
            time (int): Time taken to traverse an edge.
            change (int): Time after which signals change color.

        Returns:
            int: The second minimum time to reach from vertex 1 to vertex n.
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        dist = [[float('inf')] * 2 for _ in range(n)]
        dist[0][0] = 0

        file = deque([(0, 0)])

        while file:
            temps_courant, noeud = file.popleft()

            for voisin in adj[noeud]:
                temps_attente = 0
                if (temps_courant // change) % 2 == 1:
                    temps_attente = change - (temps_courant % change)

                nouveau_temps = time + temps_courant + temps_attente

                if dist[voisin][0] > nouveau_temps:
                    dist[voisin][1] = dist[voisin][0]
                    dist[voisin][0] = nouveau_temps
                    file.append((nouveau_temps, voisin))
                elif dist[voisin][1] > nouveau_temps and dist[voisin][0] < nouveau_temps:
                    dist[voisin][1] = nouveau_temps
                    file.append((nouveau_temps, voisin))

        return dist[n - 1][1]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.secondMinimum(5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5) == 13
    assert solution.secondMinimum(2, [[1, 2]], 3, 2) == 11
    print("All tests passed.")
