class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Removes k digits from the num string to form the smallest possible integer.

        Args:
        num: A string representing a non-negative integer.
        k: An integer indicating the number of digits to remove.

        Returns:
        A string representing the smallest possible integer after removing k digits from num.
        """
        pile = []
        for chiffre in num:
            while k and pile and pile[-1] > chiffre:
                pile.pop()
                k -= 1
            pile.append(chiffre)
        pile_final = pile[:-k] if k else pile
        return ''.join(pile_final).lstrip('0') or '0'


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.removeKdigits("1432219", 3) == "1219", "Le cas 1 a échoué"
    assert solution.removeKdigits("10200", 1) == "200", "Le cas 2 a échoué"
    assert solution.removeKdigits("10", 2) == "0", "Le cas 3 a échoué"
    assert solution.removeKdigits("112", 1) == "11", "Test supplémentaire échoué"
