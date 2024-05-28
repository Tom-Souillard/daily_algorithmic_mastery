class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        Finds the maximum length of a substring of `s` that can be changed to `t`
        with a cost less than or equal to `maxCost`.

        Args:
            s (str): The original string.
            t (str): The target string.
            maxCost (int): The maximum allowed cost to change `s` to `t`.

        Returns:
            int: The maximum length of the substring that can be changed within the budget.
        """
        debut = 0
        cout_actuel = 0
        max_longueur = 0

        for fin in range(len(s)):
            cout_actuel += abs(ord(s[fin]) - ord(t[fin]))
            while cout_actuel > maxCost:
                cout_actuel -= abs(ord(s[debut]) - ord(t[debut]))
                debut += 1
            max_longueur = max(max_longueur, fin - debut + 1)

        return max_longueur

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.equalSubstring("abcd", "bcdf", 3))  # Output: 3
    print(sol.equalSubstring("abcd", "cdef", 3))  # Output: 1
    print(sol.equalSubstring("abcd", "acde", 0))  # Output: 1
    print(sol.equalSubstring("xyz", "abc", 5))   # Output: 0
    print(sol.equalSubstring("kitten", "sitting", 10)) # Output: 3
