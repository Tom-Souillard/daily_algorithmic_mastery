class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts the given string to a zigzag pattern on a given number of rows and reads it line by line.

        Args:
        s: The input string.
        numRows: The number of rows for the zigzag pattern.

        Returns:
        The string formed by reading the zigzag pattern line by line.
        """
        if numRows == 1 or numRows >= len(s):
            return s
        ligne = [""] * numRows
        index, pas = 0, 1
        for caractere in s:
            ligne[index] += caractere
            if index == 0:
                pas = 1
            elif index == numRows - 1:
                pas = -1
            index += pas
        return "".join(ligne)


# Tests
sol = Solution()
assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert sol.convert("A", 1) == "A"
