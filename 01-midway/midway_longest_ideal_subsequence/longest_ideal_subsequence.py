class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        """
        Args:
            s (str): The input string of lowercase letters.
            k (int): Maximum allowed absolute difference in alphabet order between adjacent letters in the ideal subsequence.

        Returns:
            int: The length of the longest ideal subsequence.

        """
        from collections import defaultdict

        memoisation = defaultdict(int)
        for char in s:
            valeur_max = 0
            for i in range(max(ord(char) - k, 97), min(ord(char) + k + 1, 123)):
                valeur_max = max(valeur_max, memoisation[chr(i)])
            memoisation[char] = valeur_max + 1
        return max(memoisation.values())


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestIdealString("acfgbd", 2))  # Expected output: 4
    print(solution.longestIdealString("abcd", 3))  # Expected output: 4
    print(solution.longestIdealString("abcde", 1))  # Expected output: 5
