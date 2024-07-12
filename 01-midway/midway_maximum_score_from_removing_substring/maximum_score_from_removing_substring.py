class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Calculates the maximum points that can be gained by repeatedly removing substrings "ab" and "ba"
        from the given string s for the respective points x and y.

        Args:
            s (str): The input string.
            x (int): Points gained for removing "ab".
            y (int): Points gained for removing "ba".

        Returns:
            int: The maximum points that can be gained.
        """
        if x < y:
            x, y = y, x
            s = s[::-1]

        def remove_substrings(s: str, sub: str, points: int) -> int:
            score = 0
            stack = []
            for char in s:
                if stack and stack[-1] == sub[0] and char == sub[1]:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return score, ''.join(stack)

        score, s = remove_substrings(s, 'ab', x)
        score_y, _ = remove_substrings(s, 'ba', y)
        return score + score_y


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumGain("cdbcbbaaabab", 4, 5) == 19
    assert solution.maximumGain("aabbaaxybbaabb", 5, 4) == 20
    print("All tests passed.")
