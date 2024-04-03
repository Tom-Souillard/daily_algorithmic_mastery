from typing import List

class Solution:
    def exist(self, plateau: List[List[str]], mot: str) -> bool:
        """
        Determines if a word exists in a given board.

        Args:
            plateau: A 2D list of characters representing the board.
            mot: A string representing the word to be found.

        Returns:
            A boolean indicating whether the word exists in the board.
        """

        def chercher(i, j, k):
            if not (0 <= i < len(plateau)) or not (0 <= j < len(plateau[0])) or plateau[i][j] != mot[k]:
                return False
            if k == len(mot) - 1:
                return True

            temp, plateau[i][j] = plateau[i][j], "/"
            result = (chercher(i + 1, j, k + 1) or
                      chercher(i - 1, j, k + 1) or
                      chercher(i, j + 1, k + 1) or
                      chercher(i, j - 1, k + 1))
            plateau[i][j] = temp
            return result

        for i in range(len(plateau)):
            for j in range(len(plateau[0])):
                if chercher(i, j, 0):
                    return True
        return False


# Test case
if __name__ == "__main__":
    solution = Solution()
    plateau_test = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    mot_test = "ABCESEEEFS"
    print(solution.exist(plateau_test, mot_test))  # Expected Output: True
