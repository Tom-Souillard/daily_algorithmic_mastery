from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Calculates the cheapest price from src to dst with at most k stops.

        Args:
            n: An integer representing the number of cities.
            flights: A list of lists, where each sublist represents a flight [from, to, price].
            src: The starting city index.
            dst: The destination city index.
            k: The maximum number of stops allowed.

        Returns:
            The cheapest price as an integer. If no such route exists, returns -1.
        """
        prix = [float('inf')] * n
        prix[src] = 0

        for _ in range(k + 1):
            temp_prix = prix.copy()
            for depart, arrivee, cout in flights:
                if prix[depart] + cout < temp_prix[arrivee]:
                    temp_prix[arrivee] = prix[depart] + cout
            prix = temp_prix

        return prix[dst] if prix[dst] != float('inf') else -1
