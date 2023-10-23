from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        """
        Calcule le score maximal d'un bon sous-tableau dans un tableau donné.

        Un bon sous-tableau est un sous-tableau où i <= k <= j.
        Le score d'un sous-tableau (i, j) est défini comme min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1).

        Args:
            nums (List[int]): Le tableau d'entiers.
            k (int): L'indice k qui doit être inclus dans le bon sous-tableau.

        Returns:
            int: Le score maximal d'un bon sous-tableau.
        """
        n = len(nums)
        max_score = 0

        left, right = k, k
        min_val = nums[k]

        while left > 0 or right < n - 1:
            if left > 0 and (right == n - 1 or nums[left - 1] > nums[right + 1]):
                left -= 1
                min_val = min(min_val, nums[left])
            else:
                right += 1
                min_val = min(min_val, nums[right])

            max_score = max(max_score, min_val * (right - left + 1))

        return max(max_score, min_val * (right - left + 1))