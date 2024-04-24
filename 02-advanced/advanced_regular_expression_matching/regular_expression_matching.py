class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Determine if the input string matches the given pattern using regular expression rules.

        Args:
        s: The input string.
        p: The pattern string, which may contain '.' and '*'.

        Returns:
        A boolean indicating whether the string matches the pattern.
        """
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)
                memo[(i, j)] = ans
            return memo[(i, j)]

        return dp(0, 0)


# Test cases
solution = Solution()
assert not solution.isMatch("aa", "a"), "Test 1 Failed"
assert solution.isMatch("aa", "a*"), "Test 2 Failed"
assert solution.isMatch("ab", ".*"), "Test 3 Failed"
Re