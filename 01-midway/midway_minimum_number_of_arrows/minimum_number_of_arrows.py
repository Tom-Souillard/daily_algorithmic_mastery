from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Finds the minimum number of arrows that must be shot to burst all balloons.
        Balloons are represented by their x-coordinates on a flat wall, with each balloon
        having a start and end x-coordinate. An arrow can burst all balloons it passes
        through when shot vertically from a point on the x-axis.

        Args:
        points: A list of lists, where each inner list contains two integers
                representing the start and end x-coordinates of a balloon.

        Returns:
        The minimum number of arrows required to burst all balloons.
        """
        if not points:
            return 0

        # Sort balloons by their end x-coordinate
        points.sort(key=lambda x: x[1])
        fleches = 1
        fin_courante = points[0][1]

        for debut, fin in points:
            if debut > fin_courante:
                fleches += 1
                fin_courante = fin

        return fleches
