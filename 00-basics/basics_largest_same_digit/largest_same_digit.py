class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        Finds the largest 3-digit substring in 'num' where all digits are the same.

        Args:
        num (str): The input string representing a large integer.

        Returns:
        str: The largest 3-digit substring with the same digit, or an empty string if none exists.
        """
        meilleur = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                meilleur = max(meilleur, num[i:i + 3])
        return meilleur
