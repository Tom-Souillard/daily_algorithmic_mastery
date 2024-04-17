from typing import List
import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Given the number of nodes `n` and an undirected edge list `edges` of a tree, returns a list of all possible node labels
        that can be the root of the tree such that the tree has the minimum height.

        Args:
            n (int): The number of nodes in the tree.
            edges (List[List[int]]): A list where each element is a list of two integers representing an undirected edge in the tree.

        Returns:
            List[int]: A list containing all the labels of the minimum height trees.
        """
        if n == 1:
            return [0]
        adjacence = collections.defaultdict(set)
        for a, b in edges:
            adjacence[a].add(b)
            adjacence[b].add(a)
        feuilles = [i for i in range(n) if len(adjacence[i]) == 1]
        while n > 2:
            n -= len(feuilles)
            nouvelles_feuilles = []
            for feuille in feuilles:
                voisin = adjacence[feuille].pop()
                adjacence[voisin].remove(feuille)
                if len(adjacence[voisin]) == 1:
                    nouvelles_feuilles.append(voisin)
            feuilles = nouvelles_feuilles
        return feuilles

if __name__ == "__main__":
    sol = Solution()
    assert set(sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])) == {1}, "Test 1 failed"
    assert set(sol.findMinHeightTrees(6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]])) == {2, 3}, "Test 2 failed"
    assert set(sol.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])) == {3, 4}, "Test 3 failed"
    assert set(sol.findMinHeightTrees(1, [])) == {0}, "Test 4 failed"

    print("All tests passed!")