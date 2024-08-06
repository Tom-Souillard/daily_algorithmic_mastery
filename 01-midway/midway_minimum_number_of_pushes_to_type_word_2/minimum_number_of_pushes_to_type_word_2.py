class Solution(object):
    def minimumPushes(self, word):
        """
        Calculate the minimum number of key presses required to type a given word.

        Args:
            word (str): The word to type.

        Returns:
            int: The minimum number of key presses needed.
        """
        compteur = [0] * 26
        for lettre in word:
            indice = ord(lettre) - ord('a')
            compteur[indice] += 1

        compteur = sorted(compteur, reverse=True)
        resultat = sum(compteur[:8]) * 1
        resultat += sum(compteur[8:16]) * 2
        resultat += sum(compteur[16:24]) * 3
        resultat += sum(compteur[24:]) * 4
        return resultat


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumPushes("abcde") == 5
    assert solution.minimumPushes("xyzxyzxyzxyz") == 12
    assert solution.minimumPushes("aabbccddeeffgghhiiiiii") == 24
    print("All tests passed.")