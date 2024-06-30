class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        """
        Determine the maximum number of edges that can be removed while keeping the graph fully traversable by both Alice and Bob.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): List of edges represented as [type, node1, node2].

        Returns:
            int: The maximum number of edges that can be removed, or -1 if it's not possible to keep the graph fully traversable.
        """

        def find(parent: list[int], x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent: list[int], rank: list[int], x: int, y: int) -> bool:
            rootX = find(parent, x)
            rootY = find(parent, y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True
            return False

        parent_alice = list(range(n + 1))
        parent_bob = list(range(n + 1))
        rank_alice = [0] * (n + 1)
        rank_bob = [0] * (n + 1)

        total_edges_used = 0

        for type, u, v in edges:
            if type == 3:
                if union(parent_alice, rank_alice, u, v):
                    union(parent_bob, rank_bob, u, v)
                    total_edges_used += 1

        for type, u, v in edges:
            if type == 1:
                if union(parent_alice, rank_alice, u, v):
                    total_edges_used += 1
            elif type == 2:
                if union(parent_bob, rank_bob, u, v):
                    total_edges_used += 1

        if all(find(parent_alice, i) == find(parent_alice, 1) for i in range(1, n + 1)) and all(
                find(parent_bob, i) == find(parent_bob, 1) for i in range(1, n + 1)):
            return len(edges) - total_edges_used
        else:
            return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]) == 2
    assert solution.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]) == 0
    assert solution.maxNumEdgesToRemove(4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]]) == -1
    print("All tests passed.")
