import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Determines the furthest building index that can be reached using given bricks and ladders optimally.

        Args:
        heights: A list of integers representing the heights of buildings.
        bricks: An integer representing the number of bricks available.
        ladders: An integer representing the number of ladders available.

        Returns:
        An integer representing the furthest building index (0-indexed) that can be reached.

        The function utilizes a min-heap to keep track of the largest jumps made by bricks,
        ensuring ladders are used for the largest jumps to optimize the reach.
        """
        sauts_min_heap = []  # Min heap to store the jumps that have been made using bricks
        for i in range(len(heights) - 1):
            delta_hauteur = heights[i + 1] - heights[i]
            if delta_hauteur > 0:
                heapq.heappush(sauts_min_heap, delta_hauteur)
            if len(sauts_min_heap) > ladders:  # Use bricks for the smallest jumps
                bricks -= heapq.heappop(sauts_min_heap)
            if bricks < 0:  # If we run out of bricks, return the current index
                return i
        return len(heights) - 1  # Able to reach the last building
