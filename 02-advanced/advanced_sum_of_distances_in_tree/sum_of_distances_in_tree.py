from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Calculate the sum of distances from each node to all other nodes in an undirected tree.

        Args:
        n (int): The number of nodes in the tree.
        edges (List[List[int]]): List of edges where each edge is represented as a pair [ai, bi].

        Returns:
        List[int]: A list where the ith element is the sum of distances from node i to all other nodes.
        """
        from collections import defaultdict, deque

        if n == 1:
            return [0]

        arbre = defaultdict(list)
        for a, b in edges:
            arbre[a].append(b)
            arbre[b].append(a)

        compte = [1] * n
        resultat = [0] * n

        def dfs1(noeud, parent):
            for voisin in arbre[noeud]:
                if voisin != parent:
                    dfs1(voisin, noeud)
                    compte[noeud] += compte[voisin]
                    resultat[noeud] += resultat[voisin] + compte[voisin]

        def dfs2(noeud, parent):
            for voisin in arbre[noeud]:
                if voisin != parent:
                    resultat[voisin] = resultat[noeud] - compte[voisin] + n - compte[voisin]
                    dfs2(voisin, noeud)

        dfs1(0, -1)
        dfs2(0, -1)

        return resultat


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]) == [8, 12, 6, 10, 10, 10]
    assert solution.sumOfDistancesInTree(1, []) == [0]
    assert solution.sumOfDistancesInTree(2, [[1, 0]]) == [1, 1]
    assert solution.sumOfDistancesInTree(3, [[0, 1], [1, 2]]) == [3, 2, 3]
    print("All tests passed!")

