from typing import List
from collections import deque, defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        Finds the minimum number of buses required to travel from source to target.

        Args:
        routes: A list of lists, where each sublist represents a bus route.
        source: The starting bus stop.
        target: The destination bus stop.

        Returns:
        The minimum number of buses required to reach the target from the source, or -1 if it's not possible.
        """

        if source == target:
            return 0

        # Mapping each stop to the buses (routes) that pass through it
        arret_to_bus = defaultdict(set)
        for i, route in enumerate(routes):
            for arret in route:
                arret_to_bus[arret].add(i)

        # BFS Initialization
        visite = set([source])
        queue = deque([source])
        resultat = 0

        while queue:
            resultat += 1
            for _ in range(len(queue)):
                arret_actuel = queue.popleft()
                for bus in arret_to_bus[arret_actuel]:
                    for arret_suivant in routes[bus]:
                        if arret_suivant == target:
                            return resultat
                        if arret_suivant not in visite:
                            visite.add(arret_suivant)
                            queue.append(arret_suivant)
                    routes[bus] = []  # mark as visited

        return -1
