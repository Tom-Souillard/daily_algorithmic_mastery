from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        """
        Finds all lucky numbers in a matrix. A lucky number is defined as the minimum element
        in its row and the maximum in its column.

        Args:
            matrix (List[List[int]]): A 2D list of distinct integers representing the matrix.

        Returns:
            List[int]: A list of all lucky numbers found in the matrix.
        """
        min_lignes = {min(ligne) for ligne in matrix}
        max_colonnes = {max(colonne) for colonne in zip(*matrix)}
        return list(min_lignes & max_colonnes)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]) == [15]
    assert solution.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]) == [12]
    assert solution.luckyNumbers([[7,8],[1,2]]) == [7]
    print("All tests passed.")
