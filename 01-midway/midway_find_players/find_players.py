class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        Find players with zero or one loss in a series of matches.

        Args:
        matches: A list of lists, where each sub-list contains two integers representing the winner and loser of a match.

        Returns:
        A list containing two lists: the first list contains the players who haven't lost any match in increasing order, and the second list contains the players who have lost exactly one match in increasing order.
        """
        pertes = {}  # Dictionary to count losses
        gagnants = set()  # Set to track winners

        for gagnant, perdant in matches:
            gagnants.add(gagnant)
            if perdant not in pertes:
                pertes[perdant] = 0
            pertes[perdant] += 1

        aucune_perte = sorted(list(gagnants - pertes.keys()))
        une_perte = sorted([joueur for joueur, perte in pertes.items() if perte == 1])

        return [aucune_perte, une_perte]
