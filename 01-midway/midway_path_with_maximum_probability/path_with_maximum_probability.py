from heapq import heappush, heappop
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        """
        Calculates the maximum probability of success to traverse from start to end in an undirected graph.

        Args:
            n (int): The number of nodes in the graph.
            edges (List[List[int]]): The list of undirected edges connecting the nodes.
            succProb (List[float]): The list of success probabilities for each edge.
            start (int): The starting node.
            end (int): The destination node.

        Returns:
            float: The maximum probability of success to reach the destination node.
        """
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        prob = [0.0] * n
        prob[start] = 1.0
        heap = [(-1.0, start)]

        while heap:
            prob_actuelle, noeud = heappop(heap)
            prob_actuelle = -prob_actuelle
            if noeud == end:
                return prob_actuelle
            for voisin, p in graph[noeud]:
                nouvelle_prob = prob_actuelle * p
                if nouvelle_prob > prob[voisin]:
                    prob[voisin] = nouvelle_prob
                    heappush(heap, (-nouvelle_prob, voisin))

        return 0.0


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2) == 0.25
    assert solution.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2) == 0.3
    assert solution.maxProbability(3, [[0, 1]], [0.5], 0, 2) == 0.0
    print("All tests passed.")
