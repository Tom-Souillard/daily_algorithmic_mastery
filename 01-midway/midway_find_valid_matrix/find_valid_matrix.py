from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        Restore a matrix given row and column sums.

        Args:
        rowSum (List[int]): List of sums for each row.
        colSum (List[int]): List of sums for each column.

        Returns:
        List[List[int]]: A matrix that satisfies the row and column sums.
        """
        matrice = [[0] * len(colSum) for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                min_val = min(rowSum[i], colSum[j])
                matrice[i][j] = min_val
                rowSum[i] -= min_val
                colSum[j] -= min_val
        return matrice

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.restoreMatrix([3, 8], [4, 7]) == [[3, 0], [1, 7]], "Test case 1 failed"
    assert solution.restoreMatrix([5, 7, 10], [8, 6, 8]) == [[5, 0, 0], [3, 4, 0], [0, 2, 8]], "Test case 2 failed"
    assert solution.restoreMatrix([1, 0], [0, 1]) == [[0, 1], [0, 0]], "Test case 3 failed"
    assert solution.restoreMatrix([0, 0], [0, 0]) == [[0, 0], [0, 0]], "Test case 4 failed"
    print("All tests passed.")
