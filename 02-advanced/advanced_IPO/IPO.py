import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        """
        Find the maximum capital achievable after completing at most k projects.

        Args:
            k (int): Maximum number of projects that can be completed.
            w (int): Initial capital.
            profits (list[int]): List of profits for each project.
            capital (list[int]): List of minimum capital required for each project.

        Returns:
            int: The maximum capital after completing at most k projects.
        """
        projets = sorted(zip(capital, profits))
        disponible = []
        i = 0
        while k > 0:
            while i < len(projets) and projets[i][0] <= w:
                heapq.heappush(disponible, -projets[i][1])
                i += 1
            if not disponible:
                break
            w -= heapq.heappop(disponible)
            k -= 1
        return w

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) == 4
    assert solution.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) == 6
    assert solution.findMaximizedCapital(1, 2, [1, 2, 3], [1, 2, 3]) == 4
    print("All tests passed.")
