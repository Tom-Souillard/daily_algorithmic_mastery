from collections import defaultdict, deque
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """Returns the list of ancestors for each node in a DAG.

        Args:
            n (int): Number of nodes in the graph.
            edges (List[List[int]]): List of edges in the graph.

        Returns:
            List[List[int]]: List of ancestors for each node.
        """
        graph = defaultdict(list)
        in_degrees = [0] * n
        ancestors = [set() for _ in range(n)]

        for origine, destination in edges:
            graph[origine].append(destination)
            in_degrees[destination] += 1

        queue = deque([i for i in range(n) if in_degrees[i] == 0])

        while queue:
            noeud = queue.popleft()
            for voisin in graph[noeud]:
                ancestors[voisin].update(ancestors[noeud])
                ancestors[voisin].add(noeud)
                in_degrees[voisin] -= 1
                if in_degrees[voisin] == 0:
                    queue.append(voisin)

        return [sorted(list(ancestor)) for ancestor in ancestors]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.getAncestors(8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]) == [[],
                                                                                                                  [],
                                                                                                                  [],
                                                                                                                  [0,
                                                                                                                   1],
                                                                                                                  [0,
                                                                                                                   2],
                                                                                                                  [0, 1,
                                                                                                                   3],
                                                                                                                  [0, 1,
                                                                                                                   2, 3,
                                                                                                                   4],
                                                                                                                  [0, 1,
                                                                                                                   2,
                                                                                                                   3]]
    assert solution.getAncestors(5,
                                 [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]) == [
               [], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
    print("All tests passed.")
