from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums of unique elements, return all possible subsets (the power set).

        Args:
            nums (List[int]): A list of unique integers.

        Returns:
            List[List[int]]: A list of all possible subsets.
        """
        resultat = []

        def explorer(index, actuel):
            if index == len(nums):
                resultat.append(actuel.copy())
                return

            actuel.append(nums[index])
            explorer(index + 1, actuel)
            actuel.pop()
            explorer(index + 1, actuel)

        explorer(0, [])
        return resultat


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1, 2, 3]))  # Expected output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(solution.subsets([0]))  # Expected output: [[], [0]]
