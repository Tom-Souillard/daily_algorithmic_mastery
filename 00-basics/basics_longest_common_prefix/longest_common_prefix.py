from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix string amongst an array of strings.

        Args:
            strs (List[str]): An array of strings.

        Returns:
            str: The longest common prefix, or an empty string if there is none.
        """
        if not strs:
            return ""

        prefix = strs[0]

        for string in strs[1:]:
            i = 0
            while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
                i += 1
            prefix = prefix[:i]

            if not prefix:
                return ""

        return prefix
