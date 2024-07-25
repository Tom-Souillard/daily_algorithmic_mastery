class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        Sorts an array of integers in ascending order.

        Args:
            nums (list[int]): The array of integers to sort.

        Returns:
            list[int]: The sorted array.
        """
        def tri_fusion(tableau: list[int]) -> list[int]:
            if len(tableau) > 1:
                milieu = len(tableau) // 2
                gauche = tableau[:milieu]
                droite = tableau[milieu:]

                tri_fusion(gauche)
                tri_fusion(droite)

                i = j = k = 0
                while i < len(gauche) and j < len(droite):
                    if gauche[i] < droite[j]:
                        tableau[k] = gauche[i]
                        i += 1
                    else:
                        tableau[k] = droite[j]
                        j += 1
                    k += 1

                while i < len(gauche):
                    tableau[k] = gauche[i]
                    i += 1
                    k += 1

                while j < len(droite):
                    tableau[k] = droite[j]
                    j += 1
                    k += 1

            return tableau

        return tri_fusion(nums)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert solution.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    print("All tests passed.")
