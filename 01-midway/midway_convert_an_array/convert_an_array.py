class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """
        Create a 2D array from the given list of integers, ensuring each row has distinct integers
        and the number of rows is minimal.

        Args:
        nums (List[int]): The list of integers to convert into a 2D array.

        Returns:
        List[List[int]]: The resulting 2D array with minimal rows and distinct integers in each row.
        """
        from collections import Counter

        frequences = Counter(nums)
        matrice = []
        for valeur, freq in frequences.items():
            for i in range(freq):
                if i == len(matrice):
                    matrice.append([])
                matrice[i].append(valeur)

        return matrice
