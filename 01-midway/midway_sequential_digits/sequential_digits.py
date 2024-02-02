class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        """
        Finds all the numbers with sequential digits within a given range.

        Args:
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.

        Returns:
        List[int]: A list of all integers within the given range that have sequential digits.
        """
        resultats = []
        chiffres = "123456789"
        longueur_bas = len(str(low))
        longueur_haut = len(str(high))

        for longueur in range(longueur_bas, longueur_haut + 1):
            for debut in range(0, 10 - longueur):
                nombre = int(chiffres[debut:debut + longueur])
                if low <= nombre <= high:
                    resultats.append(nombre)

        return resultats
