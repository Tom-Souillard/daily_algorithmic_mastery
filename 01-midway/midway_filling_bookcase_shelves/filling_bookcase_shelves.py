from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """
        Calculates the minimum possible height of the bookshelf after placing all books.

        Args:
            books (List[List[int]]): List of books where each book is represented as [thickness, height].
            shelfWidth (int): The width of the shelf.

        Returns:
            int: The minimum height of the bookshelf.
        """
        n = len(books)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            largeur, hauteur_max = 0, 0
            dp[i] = float('inf')
            for j in range(i, 0, -1):
                largeur += books[j - 1][0]
                if largeur > shelfWidth:
                    break
                hauteur_max = max(hauteur_max, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + hauteur_max)

        return dp[n]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4) == 6
    assert solution.minHeightShelves([[1, 3], [2, 4], [3, 2]], 6) == 4
    assert solution.minHeightShelves([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], 3) == 3
    print("All tests passed.")
