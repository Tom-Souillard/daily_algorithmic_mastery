from typing import List


class Solution:
    def combinationSum2(self, candidats: List[int], cible: int) -> List[List[int]]:
        def rechercher_combinaisons(index: int, cible: int, chemin: List[int], resultat: List[List[int]]):
            if cible == 0:
                resultat.append(chemin)
                return
            for i in range(index, len(candidats)):
                if i > index and candidats[i] == candidats[i - 1]:
                    continue
                if candidats[i] > cible:
                    break
                rechercher_combinaisons(i + 1, cible - candidats[i], chemin + [candidats[i]], resultat)

        candidats.sort()
        resultat = []
        rechercher_combinaisons(0, cible, [], resultat)
        return resultat


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert solution.combinationSum2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]
    print("All tests passed.")
