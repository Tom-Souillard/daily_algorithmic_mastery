from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of `candidates` that sum up to `target`.

        Args:
        candidates: A list of distinct integers.
        target: An integer representing the target sum.

        Returns:
        A list of lists, where each inner list represents a unique combination of `candidates` that sums to `target`.
        """

        def dfs(i, current, total):
            if total == target:
                result.append(current.copy())
                return
            if i >= len(candidates) or total > target:
                return
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            current.pop()
            dfs(i + 1, current, total)

        result = []
        dfs(0, [], 0)
        return result


# Test cases
solution = Solution()

# Example 1
candidates1 = [2, 3, 6, 7]
target1 = 7
print(solution.combinationSum(candidates1, target1))  # Expected: [[2,2,3],[7]]

# Example 2
candidates2 = [2, 3, 5]
target2 = 8
print(solution.combinationSum(candidates2, target2))  # Expected: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3
candidates3 = [2]
target3 = 1
print(solution.combinationSum(candidates3, target3))  # Expected: []

# Additional Test
candidates4 = [1, 2]
target4 = 4
print(solution.combinationSum(candidates4, target4))  # Expected: [[1,1,1,1],[1,1,2],[2,2]]
