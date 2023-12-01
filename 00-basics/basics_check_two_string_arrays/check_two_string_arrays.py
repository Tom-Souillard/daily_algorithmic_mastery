class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        Compare two string arrays to determine if they represent the same string.

        Args:
        word1: A list of strings.
        word2: Another list of strings.

        Returns:
        A boolean indicating whether the two arrays represent the same string.

        This function iterates over the arrays character by character, ensuring minimal spatial and temporal complexity.
        """
        index_mot1, index_mot2 = 0, 0
        index_caractere1, index_caractere2 = 0, 0

        while index_mot1 < len(word1) and index_mot2 < len(word2):
            if word1[index_mot1][index_caractere1] != word2[index_mot2][index_caractere2]:
                return False

            index_caractere1 += 1
            index_caractere2 += 1

            if index_caractere1 == len(word1[index_mot1]):
                index_mot1 += 1
                index_caractere1 = 0

            if index_caractere2 == len(word2[index_mot2]):
                index_mot2 += 1
                index_caractere2 = 0

        return index_mot1 == len(word1) and index_mot2 == len(word2)


# Example usage
sol = Solution()
print(sol.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))  # Output: true
print(sol.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))  # Output: false
print(sol.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))  # Output: true
