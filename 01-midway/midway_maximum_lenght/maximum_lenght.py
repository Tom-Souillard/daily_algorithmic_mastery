class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        Find the maximum length of a concatenated string formed by a subsequence of the given array of strings, ensuring
        that the concatenated string has unique characters.

        Args:
        arr (List[str]): An array of strings.

        Returns:
        int: The maximum length of a concatenated string with unique characters.

        Example:
            Input: arr = ["un","iq","ue"]
            Output: 4
        """
        def estUnique(chaine):
            return len(set(chaine)) == len(chaine)

        def backtrack(index, courant):
            nonlocal maximum
            if index == len(arr):
                maximum = max(maximum, len(courant))
                return
            if estUnique(courant + arr[index]):
                backtrack(index + 1, courant + arr[index])
            backtrack(index + 1, courant)

        maximum = 0
        backtrack(0, "")
        return maximum
