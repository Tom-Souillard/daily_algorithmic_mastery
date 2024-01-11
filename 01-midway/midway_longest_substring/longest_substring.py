class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s: A string to be analyzed.

        Returns:
            An integer representing the length of the longest substring without repeating characters.
        """
        indiceCaractere = {}
        lePlusLong = 0
        gauche = 0

        for droite, caractere in enumerate(s):
            if caractere in indiceCaractere and indiceCaractere[caractere] >= gauche:
                gauche = indiceCaractere[caractere] + 1
            indiceCaractere[caractere] = droite
            lePlusLong = max(lePlusLong, droite - gauche + 1)

        return lePlusLong


# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # Expected output: 3
    # Test case 2
    print(solution.lengthOfLongestSubstring("bbbbb"))  # Expected output: 1
    # Test case 3
    print(solution.lengthOfLongestSubstring("pwwkew"))  # Expected output: 3
