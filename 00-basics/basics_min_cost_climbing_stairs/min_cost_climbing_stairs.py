from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Calculate the minimum cost to reach the top of the floor.

        Args:
            cost (List[int]): The cost associated with each step in the staircase.

        Returns:
            int: The minimum cost to reach the top of the floor.
        """

        cout_precedent = cost[0]
        cout_second_precedent = cost[1]

        for i in range(2, len(cost)):
            cout_actuel = min(cout_precedent, cout_second_precedent) + cost[i]
            cout_precedent, cout_second_precedent = cout_second_precedent, cout_actuel

        return min(cout_precedent, cout_second_precedent)
