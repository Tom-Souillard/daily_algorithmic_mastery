class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Given an array of integers nums and an integer target, this function finds three integers in nums such that the sum is closest to the target. It returns the sum of the three integers.

        Args:
        nums: List[int]. A list of integers.
        target: int. The target sum we want to get close to.

        Returns:
        int. The sum of the three integers closest to the target.
        """
        nums.sort()
        difference_minimale = float('inf')
        somme_proche = 0

        for i in range(len(nums) - 2):
            gauche, droite = i + 1, len(nums) - 1
            while gauche < droite:
                somme_actuelle = nums[i] + nums[gauche] + nums[droite]
                difference_actuelle = abs(target - somme_actuelle)

                if difference_actuelle < difference_minimale:
                    difference_minimale = difference_actuelle
                    somme_proche = somme_actuelle

                if somme_actuelle < target:
                    gauche += 1
                elif somme_actuelle > target:
                    droite -= 1
                else:
                    return somme_actuelle
        return somme_proche


# Test case
if __name__ == "__main__":
    solution = Solution()
    # Test 1
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    print(solution.threeSumClosest(nums1, target1))  # Expected output: 2

    # Test 2
    nums2 = [0, 0, 0]
    target2 = 1
    print(solution.threeSumClosest(nums2, target2))  # Expected output: 0

    # Test 3
    nums3 = [1, 1, -1, -1, 3]
    target3 = -1
    print(solution.threeSumClosest(nums3, target3))  # Expected output: -1 or any close value
