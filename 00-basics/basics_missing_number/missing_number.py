class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Finds the missing number in an array containing n distinct numbers in the range [0, n].

        Args:
            nums: A list of integers representing the given numbers.

        Returns:
            An integer representing the missing number in the range [0, n].
        """
        n = len(nums)
        somme_attendue = n * (n + 1) // 2
        somme_reelle = sum(nums)
        return somme_attendue - somme_reelle
