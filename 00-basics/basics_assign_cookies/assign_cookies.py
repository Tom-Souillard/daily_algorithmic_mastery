from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Finds the maximum number of children that can be contented with given cookies.

        Args:
        g (List[int]): Greed factors of the children.
        s (List[int]): Sizes of the cookies.

        Returns:
        int: Maximum number of content children.

        """
        g.sort()
        s.sort()
        enfant_index, cookie_index = 0, 0
        while enfant_index < len(g) and cookie_index < len(s):
            if s[cookie_index] >= g[enfant_index]:
                enfant_index += 1
            cookie_index += 1

        return enfant_index
