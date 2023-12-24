class Solution:
    def minOperations(self, s: str) -> int:
        """
        Calculate the minimum number of operations required to make the given string alternating.

        Args:
        s (str): The input string consisting of '0's and '1's.

        Returns:
        int: The minimum number of operations needed.
        """
        compteur1, compteur2 = 0, 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '0':
                    compteur1 += 1
                else:
                    compteur2 += 1
            else:
                if s[i] == '1':
                    compteur1 += 1
                else:
                    compteur2 += 1

        return min(compteur1, compteur2)


# Example usage
solution = Solution()
print(solution.minOperations("0100"))  # Output: 1
print(solution.minOperations("10"))  # Output: 0
print(solution.minOperations("1111"))  # Output: 2
