from typing import List


class Solution:
    def trap(self, hauteur: List[int]) -> int:
        """
        Calculate the amount of water that can be trapped after raining on a histogram.

        Args:
            hauteur (List[int]): List of non-negative integers representing the elevation map.

        Returns:
            int: Total units of trapped water.

        """
        gauche, droite = 0, len(hauteur) - 1
        max_gauche, max_droite = 0, 0
        eau = 0

        while gauche < droite:
            if hauteur[gauche] < hauteur[droite]:
                if hauteur[gauche] >= max_gauche:
                    max_gauche = hauteur[gauche]
                else:
                    eau += max_gauche - hauteur[gauche]
                gauche += 1
            else:
                if hauteur[droite] >= max_droite:
                    max_droite = hauteur[droite]
                else:
                    eau += max_droite - hauteur[droite]
                droite -= 1
        return eau


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Output: 6
    print(solution.trap([4, 2, 0, 3, 2, 5]))  # Output: 9
    print(solution.trap([3, 0, 2, 0, 4]))  # Output: 7
