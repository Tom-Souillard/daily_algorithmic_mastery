class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determines if two strings are isomorphic.

        To be isomorphic, all occurrences of a character in `s` can be replaced to get `t`, maintaining the order of characters. No two characters may map to the same character unless they are identical.

        Args:
        s: First string to compare.
        t: Second string to compare.

        Returns:
        A boolean indicating whether the strings are isomorphic.
        """
        if len(s) != len(t):
            return False
        mapping_s_to_t, mapping_t_to_s = {}, {}
        for caractere_s, caractere_t in zip(s, t):
            if (caractere_s in mapping_s_to_t and mapping_s_to_t[caractere_s] != caractere_t) or (caractere_t in mapping_t_to_s and mapping_t_to_s[caractere_t] != caractere_s):
                return False
            mapping_s_to_t[caractere_s] = caractere_t
            mapping_t_to_s[caractere_t] = caractere_s
        return True

# Partie test
if __name__ == "__main__":
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))  # True
    print(solution.isIsomorphic("foo", "bar"))  # False
    print(solution.isIsomorphic("paper", "title"))  # True
    print(solution.isIsomorphic("badc", "baba"))  # False
