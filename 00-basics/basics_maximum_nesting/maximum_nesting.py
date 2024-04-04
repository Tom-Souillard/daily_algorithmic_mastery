class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Finds the maximum depth of nested parentheses in a valid parentheses string.

        Args:
        s: A string representing a valid parentheses sequence.

        Returns:
        The maximum nesting depth of the parentheses in the string.

        """
        profondeur_max = 0
        compteur = 0
        for caractere in s:
            if caractere == '(':
                compteur += 1
                profondeur_max = max(profondeur_max, compteur)
            elif caractere == ')':
                compteur -= 1
        return profondeur_max


# Test
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDepth("(1+(2*3)+((8)/4))+1"))  # Output: 3
    print(solution.maxDepth("(1)+((2))+(((3)))"))  # Output: 3
    print(solution.maxDepth("1+(2*3)/(2-1)"))  # Output: 1
    print(solution.maxDepth("1"))  # Output: 0
