class Solution:
    def nearestPalindromic(self, n: str) -> str:
        """
        Returns the closest palindromic integer to the given integer represented as a string.

        Args:
            n (str): The input number as a string.

        Returns:
            str: The closest palindromic number as a string.
        """
        nombre = int(n)
        if nombre == 1:
            return "0"

        taille = len(n)
        haut = 10 ** taille + 1
        bas = 10 ** (taille - 1) - 1

        prefixe = int(n[:(taille + 1) // 2])

        # Generate candidates
        candidats = set()
        for delta in [-1, 0, 1]:
            new_prefixe = str(prefixe + delta)
            if taille % 2 == 0:
                candidat = new_prefixe + new_prefixe[::-1]
            else:
                candidat = new_prefixe + new_prefixe[:-1][::-1]
            candidats.add(candidat)

        candidats.add(str(haut))
        candidats.add(str(bas))
        candidats.discard(n)

        # Find the closest palindrome
        return min(candidats, key=lambda x: (abs(int(x) - nombre), int(x)))


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.nearestPalindromic("123") == "121"
    assert solution.nearestPalindromic("1") == "0"
    assert solution.nearestPalindromic("9") == "8"
    assert solution.nearestPalindromic("11") == "9"
    assert solution.nearestPalindromic("100") == "99"
    assert solution.nearestPalindromic("101") == "99"
    assert solution.nearestPalindromic("10") == "9"
    assert solution.nearestPalindromic("999") == "1001"
    assert solution.nearestPalindromic("1213") == "1221"
    assert solution.nearestPalindromic("998") == "999"
    assert solution.nearestPalindromic("10987") == "11011"
    print("All tests passed.")
