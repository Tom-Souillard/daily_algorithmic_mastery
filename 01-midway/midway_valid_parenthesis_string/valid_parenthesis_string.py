class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Determines if the given string is valid according to the specified rules.

        Args:
        s: A string consisting of '(', ')', and '*' characters.

        Returns:
        A boolean indicating if the string is valid.

        The function uses a greedy approach, keeping track of the balance of parentheses with the ability to
        substitute '*' for either parenthesis or an empty string. It ensures that at any point, the sequence
        can still form a valid string considering the flexibility offered by '*'.
        """
        gauche_min, gauche_max = 0, 0
        for caractere in s:
            if caractere == '(':
                gauche_min += 1
                gauche_max += 1
            elif caractere == ')':
                gauche_min = max(gauche_min - 1, 0)
                gauche_max -= 1
                if gauche_max < 0:
                    return False
            else:
                gauche_min = max(gauche_min - 1, 0)
                gauche_max += 1
        return gauche_min == 0


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.checkValidString("()") == True, "Test 1 Échoué"
    assert solution.checkValidString("(*)") == True, "Test 2 Échoué"
    assert solution.checkValidString("(*))") == True, "Test 3 Échoué"
    # Tests supplémentaires
    assert solution.checkValidString("") == True, "Test 4 Échoué"
    assert solution.checkValidString("(*()") == True, "Test 5 Échoué"
    assert solution.checkValidString(")*(") == False, "Test 6 Échoué"
    print("Tous les tests ont réussi!")