class Solution:
    def numberToWords(self, num: int) -> str:
        """
        Converts a non-negative integer to its English words representation.

        Args:
            num: A non-negative integer.

        Returns:
            The English words representation of the integer.
        """
        moins_de_vingt = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                          "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                          "Eighteen", "Nineteen"]
        dizaines = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        milles = ["", "Thousand", "Million", "Billion"]

        if num == 0:
            return "Zero"

        def helper(n: int) -> str:
            if n == 0:
                return ""
            elif n < 20:
                return moins_de_vingt[n] + " "
            elif n < 100:
                return dizaines[n // 10] + " " + helper(n % 10)
            elif n < 1000:
                return moins_de_vingt[n // 10**2] + " Hundred " + helper(n % 10**2)
            else:
                for i, mot in enumerate(milles):
                    if n < 1000**(i + 1):
                        return helper(n // 1000**i) + mot + " " + helper(n % 1000**i)

        return helper(num).strip()

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.numberToWords(123) == "One Hundred Twenty Three"
    assert solution.numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"
    assert solution.numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    assert solution.numberToWords(0) == "Zero"
    assert solution.numberToWords(100) == "One Hundred"
    print("All tests passed.")
