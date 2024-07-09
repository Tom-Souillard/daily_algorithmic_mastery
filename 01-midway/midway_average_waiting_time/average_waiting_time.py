from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """
        Calculates the average waiting time for a list of customers.

        Args:
            customers: A list of lists, where each sublist contains the arrival time and the time required to prepare the order.

        Returns:
            The average waiting time of all customers.
        """
        temps_total = 0
        temps_actuel = 0

        for arrivee, temps in customers:
            if temps_actuel < arrivee:
                temps_actuel = arrivee
            temps_actuel += temps
            temps_total += temps_actuel - arrivee

        return temps_total / len(customers)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.averageWaitingTime([[1, 2], [2, 5], [4, 3]]) == 5.0
    assert solution.averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]) == 3.25
    print("All tests passed.")
