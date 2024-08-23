from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        """
        Compute the sum of fractions in a given string expression and return the result
        as an irreducible fraction in string format.

        Args:
            expression (str): A string representing a mathematical expression involving
                              the addition and subtraction of fractions.

        Returns:
            str: The irreducible fraction result of the expression.
        """
        fractions = expression.replace('-', '+-').split('+')
        resultat = sum(Fraction(fr) for fr in fractions if fr)
        return f"{resultat.numerator}/{resultat.denominator}"

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.fractionAddition("-1/2+1/2") == "0/1"
    assert solution.fractionAddition("-1/2+1/2+1/3") == "1/3"
    assert solution.fractionAddition("1/3-1/2") == "-1/6"
    print("All tests passed.")
