class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        Reverse the prefix of the word up to and including the first occurrence of the character `ch`.

        Args:
        word (str): The string in which to perform the operation.
        ch (str): The character to search for in `word`.

        Returns:
        str: The modified string after reversing the prefix up to the first occurrence of `ch`.
        """
        index = word.find(ch)
        if index == -1:
            return word
        return word[:index + 1][::-1] + word[index + 1:]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.reversePrefix("abcdefd", "d") == "dcbaefd"
    assert sol.reversePrefix("xyxzxe", "z") == "zxyxxe"
    assert sol.reversePrefix("abcd", "z") == "abcd"