from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        """
        Find the element that appears more than 25% of the time in a sorted array.

        Args:
        arr (List[int]): A sorted integer array.

        Returns:
        int: The integer that occurs more than 25% in the array.

        """
        taille_limite = len(arr) // 4
        compteur = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                compteur += 1
                if compteur > taille_limite:
                    return arr[i]
            else:
                compteur = 1

        return arr[0]

# Exemple d'utilisation
solution = Solution()
print(solution.findSpecialInteger([1,2,2,6,6,6,6,7,10]))  # Devrait retourner 6
print(solution.findSpecialInteger([1,1]))  # Devrait retourner 1
