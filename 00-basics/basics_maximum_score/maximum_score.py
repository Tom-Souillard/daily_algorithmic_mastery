class Solution:
    def maxScore(self, s: str) -> int:
        """
        Calculate the maximum score after splitting the string into two non-empty substrings.
        The score is the number of zeros in the left substring plus the number of ones in the right substring.

        Args:
        s (str): The input string consisting of zeros and ones.

        Returns:
        int: The maximum score possible after splitting the string.
        """
        total_ones = s.count('1')
        zeros_gauche, score_max = 0, 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_gauche += 1
            else:
                total_ones -= 1
            score_max = max(score_max, zeros_gauche + total_ones)

        return score_max
