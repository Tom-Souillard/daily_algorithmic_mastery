from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        """
        Eliminate the maximum number of monsters before any reaches the city.

        Given the distance of each monster from the city and their speed, calculate
        the maximum number of monsters that can be eliminated before one reaches
        the city, using a weapon that charges for one minute between shots.

        Args:
        dist: A list of integers where dist[i] is the initial distance of the i-th monster.
        speed: A list of integers where speed[i] is the speed of the i-th monster.

        Returns:
        An integer representing the maximum number of monsters that can be eliminated.
        """

        temps_arrivee = [dist[i] / speed[i] for i in range(len(dist))]
        temps_arrivee.sort()
        monstres_elimines = 0

        for i, temps in enumerate(temps_arrivee):
            if i >= temps:
                break
            monstres_elimines += 1
        return monstres_elimines