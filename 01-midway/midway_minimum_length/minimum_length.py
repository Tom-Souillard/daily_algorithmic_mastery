class Solution:
    def minimumLength(self, s: str) -> int:
        """
        Calculates the minimum length of a string after repeatedly deleting non-intersecting
        prefix and suffix with the same character.

        Args:
        s: A string consisting of only 'a', 'b', and 'c'.

        Returns:
        The minimum length of the string after performing the deletion operation any number of times.

        The function utilizes two pointers to scan from both ends of the string towards the center,
        removing matching prefixes and suffixes. The operation stops when either the string is empty,
        or there are no matching characters at the two ends.
        """
        gauche = 0
        droite = len(s) - 1

        while gauche < droite and s[gauche] == s[droite]:
            caractere_actuel = s[gauche]
            while gauche <= droite and s[gauche] == caractere_actuel:
                gauche += 1
            while droite >= gauche and s[droite] == caractere_actuel:
                droite -= 1

        return droite - gauche + 1
