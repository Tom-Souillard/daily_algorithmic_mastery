class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        Traverse a 2D integer array in diagonal order.

        This function takes a 2D integer array 'nums' and returns all its elements in a diagonal
        order. The traversal is done in a way to mimic the diagonal reading of the matrix, starting
        from the top left corner and moving towards the bottom right corner.

        Args:
            nums: A 2D integer array representing the matrix to be traversed.

        Returns:
            A list of integers representing the elements of 'nums' in the diagonal traversal order.
        """
        diagonales = defaultdict(list)
        for i, ligne in enumerate(nums):
            for j, valeur in enumerate(ligne):
                diagonales[i + j].append(valeur)

        resultat = []
        for k in sorted(diagonales.keys()):
            resultat.extend(reversed(diagonales[k]))

        return resultat
