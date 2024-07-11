class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        Reverse the substrings in each pair of matching parentheses, starting from the innermost one.

        Args:
            s (str): The input string containing lowercase English letters and parentheses.

        Returns:
            str: The modified string with the substrings reversed as described.
        """
        pile = []
        for char in s:
            if char == ')':
                sous_chaine = []
                while pile and pile[-1] != '(':
                    sous_chaine.append(pile.pop())
                pile.pop()
                pile.extend(sous_chaine)
            else:
                pile.append(char)
        return ''.join(pile)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.reverseParentheses("(abcd)") == "dcba"
    assert solution.reverseParentheses("(u(love)i)") == "iloveu"
    assert solution.reverseParentheses("(ed(et(oc))el)") == "leetcode"
    print("All tests passed.")
