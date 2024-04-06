class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Removes the minimum number of parentheses to make the input string valid.

        Args:
            s: A string consisting of '(', ')', and lowercase English characters.

        Returns:
            A string where the minimum number of parentheses have been removed to make it valid.
        """
        indices_a_supprimer, pile = set(), []
        for indice, char in enumerate(s):
            if char == '(':
                pile.append(indice)
            elif char == ')':
                if pile:
                    pile.pop()
                else:
                    indices_a_supprimer.add(indice)
        indices_a_supprimer = indices_a_supprimer.union(set(pile))
        return ''.join(char for indice, char in enumerate(s) if indice not in indices_a_supprimer)

# Partie test
if __name__ == "__main__":
    solution = Solution()
    assert solution.minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
    assert solution.minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
    assert solution.minRemoveToMakeValid("))((") == ""
    assert solution.minRemoveToMakeValid("(a(b)c)d)") == "(a(b)c)d"
