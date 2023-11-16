class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Finds a binary string of length n that does not appear in the given array of n unique binary strings.

        Args:
        nums (List[str]): An array of n unique binary strings each of length n.

        Returns:
        str: A binary string of length n that is not present in nums.
        """
        longueur = len(nums)
        chaine_binaire_diff = ''

        for i in range(longueur):
            chaine_binaire_diff += '1' if nums[i][i] == '0' else '0'

        return chaine_binaire_diff