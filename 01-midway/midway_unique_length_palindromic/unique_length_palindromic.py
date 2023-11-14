class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Counts the number of unique palindromic subsequences of length three in a given string.

        Args:
        s (str): The input string.

        Returns:
        int: The number of unique palindromic subsequences of length three.
        """
        resultat = set()
        premierIndex, dernierIndex = {}, {}

        for index, caractere in enumerate(s):
            dernierIndex[caractere] = index
            if caractere not in premierIndex:
                premierIndex[caractere] = index

        for caractere in premierIndex:
            if dernierIndex[caractere] - premierIndex[caractere] >= 2:
                for charMilieu in set(s[premierIndex[caractere] + 1:dernierIndex[caractere]]):
                    resultat.add((caractere, charMilieu, caractere))

        return len(resultat)


# Example usage:
sol = Solution()
print(sol.countPalindromicSubsequence("aabca"))  # Output: 3
