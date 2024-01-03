class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        Calculates the total number of laser beams in a bank. A beam is formed between security devices
        on different rows with no intervening security devices.

        Args:
        bank: List[str] - A list of strings representing the bank's floor plan. Each string is a binary
                          representation of a row in the bank, where '1' and '0' represent a security
                          device and an empty cell, respectively.

        Returns:
        int: The total number of laser beams formed in the bank.
        """
        nombreDeDispositifs = [ligne.count('1') for ligne in bank]
        totalFaisceaux = 0
        faisceauPrecedent = 0

        for dispositif in nombreDeDispositifs:
            if dispositif:
                totalFaisceaux += faisceauPrecedent * dispositif
                faisceauPrecedent = dispositif

        return totalFaisceaux
