from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        """
        Find the widest vertical area between points on a 2D plane.

        Args:
        points: A list of lists where each sublist contains the x and y coordinates of a point.

        Returns:
        The maximum width of a vertical area between two points such that no points are inside the area.

        The function first extracts the x-coordinates of the points, sorts them, and then finds the maximum gap between consecutive x-coordinates.
        """
        # Extract and sort the x-coordinates
        x_coords = sorted(point[0] for point in points)

        # Initialize the maximum gap
        max_gap = 0

        # Iterate through the sorted x-coordinates to find the maximum gap
        for i in range(1, len(x_coords)):
            max_gap = max(max_gap, x_coords[i] - x_coords[i - 1])

        return max_gap


# Example usage
solution = Solution()
print(solution.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]))  # Expected output: 1
print(solution.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))  # Expected output: 3
