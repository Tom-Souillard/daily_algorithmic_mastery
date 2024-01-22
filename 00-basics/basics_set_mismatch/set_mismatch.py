class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Find the number that occurs twice and the number that is missing in the array.

        This function takes an array of integers where one number is duplicated and
        one number from 1 to n is missing (n being the length of the array). It returns
        a list containing the duplicated number and the missing number.

        Args:
        nums: A list of integers where one number is duplicated and one is missing.

        Returns:
        A list containing two integers: the duplicated number and the missing number.
        """
        doublon = sum(nums) - sum(set(nums))
        n = len(nums)
        total = n * (n + 1) // 2
        manquant = total - sum(set(nums))

        return [doublon, manquant]
