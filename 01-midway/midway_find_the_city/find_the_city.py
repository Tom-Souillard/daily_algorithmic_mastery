class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        """
        Find the city with the smallest number of neighbors at a given distance threshold.

        Args:
            n (int): Number of cities.
            edges (list[list[int]]): List of edges where each edge is represented as [from, to, weight].
            distanceThreshold (int): The maximum distance to consider.

        Returns:
            int: The city with the smallest number of neighbors within the distance threshold. If there
            are multiple such cities, return the city with the greatest number.
        """
        inf = float('inf')
        distances = [[inf] * n for _ in range(n)]

        for i in range(n):
            distances[i][i] = 0

        for fromi, toi, weighti in edges:
            distances[fromi][toi] = weighti
            distances[toi][fromi] = weighti

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distances[i][k] + distances[k][j] < distances[i][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]

        min_neighbor_count = inf
        result_city = -1

        for i in range(n):
            count = sum(1 for j in range(n) if distances[i][j] <= distanceThreshold)
            if count < min_neighbor_count or (count == min_neighbor_count and i > result_city):
                min_neighbor_count = count
                result_city = i

        return result_city


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4) == 3
    assert solution.findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2) == 0
    print("All tests passed.")
