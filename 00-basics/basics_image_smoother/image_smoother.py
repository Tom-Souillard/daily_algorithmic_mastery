from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """
        Apply a 3x3 smoothing filter to each cell of a grayscale image.

        Args:
        img (List[List[int]]): The input image represented as a 2D matrix of integers.

        Returns:
        List[List[int]]: The smoothed image represented as a 2D matrix of integers.
        """

        def calculMoyenne(i, j):
            somme, count = 0, 0
            for x in range(max(0, i - 1), min(m, i + 2)):
                for y in range(max(0, j - 1), min(n, j + 2)):
                    somme += img[x][y]
                    count += 1
            return somme // count

        m, n = len(img), len(img[0])
        resultat = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                resultat[i][j] = calculMoyenne(i, j)

        return resultat
