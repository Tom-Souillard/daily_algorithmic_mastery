from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique quadruplets in the array which gives the sum of target.

        Args:
        nums: List[int] - A list of integers.
        target: int - The target sum of the quadruplets.

        Returns:
        List[List[int]] - A list of lists of integers representing all unique quadruplets that sum up to the target.
        """
        nums.sort()
        resultat, n = [], len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                gauche, droite = j + 1, n - 1
                while gauche < droite:
                    somme = nums[i] + nums[j] + nums[gauche] + nums[droite]
                    if somme < target:
                        gauche += 1
                    elif somme > target:
                        droite -= 1
                    else:
                        resultat.append([nums[i], nums[j], nums[gauche], nums[droite]])
                        while gauche < droite and nums[gauche] == nums[gauche+1]:
                            gauche += 1
                        while gauche < droite and nums[droite] == nums[droite-1]:
                            droite -= 1
                        gauche += 1
                        droite -= 1
        return resultat

# Test part
if __name__ == "__main__":
    solution = Solution()
    assert set(tuple(sorted(sub)) for sub in solution.fourSum([1,0,-1,0,-2,2], 0)) == set([(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)])
    assert set(tuple(sorted(sub)) for sub in solution.fourSum([2,2,2,2,2], 8)) == set([(2, 2, 2, 2)])
