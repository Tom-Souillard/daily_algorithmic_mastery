from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        Calculate the minimum time to visit all points on a 2D plane.

        Args:
        points: A list of lists, where each inner list contains two integers
                representing the x and y coordinates of a point on a 2D plane.

        Returns:
        int: The minimum time in seconds to visit all the points in order.
        """
        temps_total = 0
        for i in range(len(points) - 1):
            point_actuel = points[i]
            point_suivant = points[i + 1]
            temps_total += max(abs(point_suivant[0] - point_actuel[0]), abs(point_suivant[1] - point_actuel[1]))
        return temps_total
