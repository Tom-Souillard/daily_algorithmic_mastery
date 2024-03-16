class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the given list that sum up to zero.

        Args:
            nums: A list of integers.

        Returns:
            A list of lists, where each inner list contains three integers that sum up to zero. These triplets are unique, with no duplicate triplets in the output.

        """
        nums.sort()
        resultat = []
        taille = len(nums)
        for i in range(taille):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            gauche, droite = i + 1, taille - 1
            while gauche < droite:
                somme = nums[i] + nums[gauche] + nums[droite]
                if somme < 0:
                    gauche += 1
                elif somme > 0:
                    droite -= 1
                else:
                    resultat.append([nums[i], nums[gauche], nums[droite]])
                    while gauche < droite and nums[gauche] == nums[gauche + 1]:
                        gauche += 1
                    while gauche < droite and nums[droite] == nums[droite - 1]:
                        droite -= 1
                    gauche += 1
                    droite -= 1
        return resultat

# Test case
if __name__ == "__main__":
    solution = Solution()
    assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]], "Le test 1 a échoué"
    assert solution.threeSum([0, 1, 1]) == [], "Le test 2 a échoué"
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]], "Le test 3 a échoué"
    assert solution.threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]], "Le test 4 a échoué"
