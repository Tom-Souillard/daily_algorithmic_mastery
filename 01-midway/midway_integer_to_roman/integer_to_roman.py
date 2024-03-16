class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Converts an integer to a Roman numeral.

        Args:
            num: An integer to be converted.

        Returns:
            A string representing the Roman numeral equivalent of the integer.
        """
        valeurs = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                   (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        resultat = ""
        for valeur, symbole in valeurs:
            while num >= valeur:
                resultat += symbole
                num -= valeur
        return resultat

# Partie test
if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(3))  # "III"
    print(solution.intToRoman(58))  # "LVIII"
    print(solution.intToRoman(1994))  # "MCMXCIV"
    print(solution.intToRoman(4))  # "IV"
    print(solution.intToRoman(9))  # "IX"
    print(solution.intToRoman(40))  # "XL"


