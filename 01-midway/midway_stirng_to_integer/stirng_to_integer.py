class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Converts a string to a 32-bit signed integer.

        Args:
        s: A string containing the integer representation.

        Returns:
        An integer converted from string following specific rules. Clamps the result within 32-bit signed integer range.
        """
        index, signe, resultat = 0, 1, 0
        maxInt, minInt = 2 ** 31 - 1, -2 ** 31

        while index < len(s) and s[index] == ' ':
            index += 1

        if index < len(s) and s[index] == '-':
            signe = -1
            index += 1
        elif index < len(s) and s[index] == '+':
            index += 1

        while index < len(s) and s[index].isdigit():
            resultat = resultat * 10 + int(s[index])
            index += 1

        resultat *= signe

        if resultat < minInt:
            return minInt
        if resultat > maxInt:
            return maxInt

        return resultat


# Test cases
sol = Solution()

assert sol.myAtoi("42") == 42
assert sol.myAtoi("   -42") == -42
assert sol.myAtoi("4193 with words") == 4193
assert sol.myAtoi("words and 987") == 0
assert sol.myAtoi("-91283472332") == -2 ** 31
