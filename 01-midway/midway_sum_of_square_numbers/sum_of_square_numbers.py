class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Determines whether there are two integers a and b such that a^2 + b^2 equals the given non-negative integer c.

        Args:
            c (int): A non-negative integer.

        Returns:
            bool: True if there exist two integers a and b such that a^2 + b^2 = c, otherwise False.
        """
        import math
        gauche = 0
        droit = int(math.sqrt(c))
        while gauche <= droit:
            somme = gauche * gauche + droit * droit
            if somme == c:
                return True
            elif somme < c:
                gauche += 1
            else:
                droit -= 1
        return False

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.judgeSquareSum(5) == True
    assert solution.judgeSquareSum(3) == False
    assert solution.judgeSquareSum(4) == True
    assert solution.judgeSquareSum(2) == True
    assert solution.judgeSquareSum(1) == True
    assert solution.judgeSquareSum(0) == True
    print("All tests passed.")
