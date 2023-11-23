from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of elements in 'candidates' that sum to 'target'.
        Each element in 'candidates' may only be used once in the combination.

        Args:
        candidates: A list of integers representing the candidate numbers.
        target: An integer representing the target sum.

        Returns:
        A list of lists, with each inner list representing a unique combination of
        numbers that sum up to 'target'. The solution set contains no duplicate combinations.
        """
        candidates.sort()
        resultat = []

        def backtrack(debut, chemin, total):
            if total == target:
                resultat.append(chemin[:])
                return
            if total > target:
                return

            precedent = -1
            for i in range(debut, len(candidates)):
                if candidates[i] == precedent:
                    continue
                chemin.append(candidates[i])
                backtrack(i + 1, chemin, total + candidates[i])
                chemin.pop()
                precedent = candidates[i]

        backtrack(0, [], 0)
        return resultat


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    # Expected: [[1,1,6], [1,2,5], [1,7], [2,6]]
    print(solution.combinationSum2([2, 5, 2, 1, 2], 5))
    # Expected: [[1,2,2], [5]]
    print(solution.combinationSum2([3, 1, 3, 5, 1], 8))
    # Expected: [[1,1,3,3], [3,5]]
