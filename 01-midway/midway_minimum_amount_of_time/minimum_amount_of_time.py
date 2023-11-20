class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        """
        Calculate the minimum time required to collect all garbage.

        Args:
        garbage (List[str]): List of strings representing garbage types at each house.
        travel (List[int]): List of travel times between consecutive houses.

        Returns:
        int: Minimum total time to collect all garbage.

        The function iterates through the garbage list once, keeping track of the last
        occurrence of each garbage type. The total time is calculated by summing up the
        garbage collection time and the travel time to the last house for each type.
        """
        dernier_maison_metal, dernier_maison_papier, dernier_maison_verre = -1, -1, -1
        temps_total = 0

        # Iterate to find the last house with each type of garbage
        for i, maison in enumerate(garbage):
            if 'M' in maison:
                dernier_maison_metal = i
            if 'P' in maison:
                dernier_maison_papier = i
            if 'G' in maison:
                dernier_maison_verre = i

            # Add collection time
            temps_total += len(maison)

        # Add travel time
        for i in range(max(dernier_maison_metal, dernier_maison_papier, dernier_maison_verre)):
            if i < dernier_maison_metal:
                temps_total += travel[i]
            if i < dernier_maison_papier:
                temps_total += travel[i]
            if i < dernier_maison_verre:
                temps_total += travel[i]

        return temps_total