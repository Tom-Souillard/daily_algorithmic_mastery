class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        Determines if the two halves of a given string have the same number of vowels.

        Args:
        s (str): The input string, which is of even length.

        Returns:
        bool: True if both halves of the string have the same number of vowels, False otherwise.
        """

        def compterVoyelles(chaine):
            return sum(1 for char in chaine if char in 'aeiouAEIOU')

        moitie = len(s) // 2
        return compterVoyelles(s[:moitie]) == compterVoyelles(s[moitie:])


# Example usage
sol = Solution()
print(sol.halvesAreAlike("book"))  # True
print(sol.halvesAreAlike("textbook"))  # False
