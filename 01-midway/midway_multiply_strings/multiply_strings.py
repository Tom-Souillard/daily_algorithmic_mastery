class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Multiplies two non-negative integers represented as strings and returns the product also as a string.

        Args:
        num1 (str): The first number as a string.
        num2 (str): The second number as a string.

        Returns:
        str: The product of num1 and num2 as a string.
        """
        if num1 == "0" or num2 == "0":
            return "0"
        longueur1 = len(num1)
        longueur2 = len(num2)
        resultats = [0] * (longueur1 + longueur2)
        for i in range(longueur1 - 1, -1, -1):
            for j in range(longueur2 - 1, -1, -1):
                multiplication = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                somme = multiplication + resultats[i + j + 1]
                resultats[i + j] += somme // 10
                resultats[i + j + 1] = somme % 10
        resultat_final = ''.join(map(str, resultats))
        return resultat_final.lstrip('0')

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.multiply("2", "3") == "6", "Le test avec 2 et 3 a échoué."
    assert solution.multiply("123", "456") == "56088", "Le test avec 123 et 456 a échoué."
    assert solution.multiply("0", "12345") == "0", "Le test avec 0 et 12345 a échoué."
    assert solution.multiply("999", "999") == "998001", "Le test avec 999 et 999 a échoué."
