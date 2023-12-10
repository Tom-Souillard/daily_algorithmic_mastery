class Solution:
    def transpose(self, matrice: List[List[int]]) -> List[List[int]]:
        """
        Transpose the given 2D matrix.

        This method transposes a given 2D matrix, flipping it over its main diagonal.
        This results in switching the matrix's row and column indices.

        Args:
            matrice: A 2D list of integers representing the matrix to be transposed.

        Returns:
            A 2D list of integers representing the transposed matrix.
        """
        return [[matrice[i][j] for i in range(len(matrice))] for j in range(len(matrice[0]))]