class Solution:
    def numberOfWays(self, corridor: str) -> int:
        """
        Calculate the number of ways to divide a corridor into sections,
        each containing exactly two seats, separated by plants.

        Args:
        corridor (str): A string representing the corridor,
                        where 'S' is a seat and 'P' is a plant.

        Returns:
        int: The number of ways to divide the corridor, modulo 10^9 + 7.
        """
        nbSieges, resultat, nbPlantes = 0, 1, 0
        for i in corridor:
            if i == 'S':
                nbSieges += 1
            else:
                if nbSieges == 2:
                    nbPlantes += 1
            if nbSieges == 3:
                resultat = resultat * (nbPlantes + 1) % (10**9 + 7)
                nbSieges, nbPlantes = 1, 0
        if nbSieges != 2:
            return 0
        return resultat