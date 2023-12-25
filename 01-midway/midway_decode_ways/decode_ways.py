class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Calculates the number of ways to decode a given string of digits into letters,
        adhering to the mapping 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26.

        Args:
        s (str): The string containing only digits to be decoded.

        Returns:
        int: The number of ways to decode the string.

        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(1), constant space used.
        """

        # Handling edge cases
        if not s or s[0] == '0':
            return 0

        # Initialization for the bottom-up approach
        precedent, actuel = 1, 1

        for i in range(1, len(s)):
            temp = actuel

            # Check for valid two-digit letter
            if s[i] == '0':
                if s[i - 1] not in '12':
                    return 0
                actuel = precedent
            elif 10 <= int(s[i - 1:i + 1]) <= 26:
                actuel += precedent

            precedent = temp

        return actuel
