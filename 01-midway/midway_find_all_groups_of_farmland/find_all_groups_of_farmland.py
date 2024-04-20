from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        """
        This function takes a binary matrix 'land' where 1s represent farmland and 0s represent forested land. It finds all rectangular groups of connected farmland and returns the coordinates of their top-left and bottom-right corners.

        Args:
        land (List[List[int]]): The matrix representing the land, where 1 is farmland and 0 is forest.

        Returns:
        List[List[int]]: A list of lists, where each sublist contains four integers [r1, c1, r2, c2], representing the row and column of the top-left and bottom-right corners of each group of farmland.
        """
        m, n = len(land), len(land[0])
        result = []
        visite = [[False] * n for _ in range(m)]

        def explore(r, c):
            r2, c2 = r, c
            while r2 < m and land[r2][c] == 1:
                c_temp = c
                while c_temp < n and land[r2][c_temp] == 1:
                    visite[r2][c_temp] = True
                    c_temp += 1
                c2 = max(c2, c_temp - 1)
                r2 += 1
            for i in range(r, r2):
                for j in range(c, c2 + 1):
                    if not visite[i][j]:
                        return False
            return [r, c, r2 - 1, c2]

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and not visite[i][j]:
                    res = explore(i, j)
                    if res:
                        result.append(res)
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    land1 = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
    assert solution.findFarmland(land1) == [[0, 0, 0, 0], [1, 1, 2, 2]]
    land2 = [[1, 1], [1, 1]]
    assert solution.findFarmland(land2) == [[0, 0, 1, 1]]
    land3 = [[0]]
    assert solution.findFarmland(land3) == []
