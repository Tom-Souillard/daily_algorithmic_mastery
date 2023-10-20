from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible permutations of a given list of distinct integers.

        Args:
        nums: A list of distinct integers.

        Returns:
        A list of lists, where each list represents a permutation of the input list.
        """
        resultats = []

        def backtrack(debut, fin):
            if debut == fin:
                resultats.append(nums.copy())
            for i in range(debut, fin):
                nums[debut], nums[i] = nums[i], nums[debut]
                backtrack(debut + 1, fin)
                nums[debut], nums[i] = nums[i], nums[debut]

        backtrack(0, len(nums))
        return resultats


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1, 2, 3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(solution.permute([0, 1]))  # [[0,1],[1,0]]
    print(solution.permute([1]))  # [[1]]
    print(solution.permute([1, 2]))  # [[1,2],[2,1]]
