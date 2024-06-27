class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        """
        Find the center of a star graph given its edges.

        Args:
            edges (list[list[int]]): A list of edges where each edge is represented by a list of two integers.

        Returns:
            int: The center node of the star graph.
        """
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.findCenter([[1, 2], [2, 3], [4, 2]]) == 2
    assert solution.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]) == 1
    print("All tests passed.")
