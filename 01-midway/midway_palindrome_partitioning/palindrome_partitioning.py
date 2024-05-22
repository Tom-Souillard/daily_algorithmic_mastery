from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Partition the input string such that every substring in the partition is a palindrome.

        Args:
        s (str): The string to partition.

        Returns:
        List[List[str]]: All possible palindrome partitionings of the input string.
        """

        def est_palindrome(debut, fin):
            while debut < fin:
                if s[debut] != s[fin]:
                    return False
                debut, fin = debut + 1, fin - 1
            return True

        def backtrack(debut, chemin):
            if debut == len(s):
                resultat.append(chemin[:])
                return
            for fin in range(debut, len(s)):
                if est_palindrome(debut, fin):
                    chemin.append(s[debut:fin + 1])
                    backtrack(fin + 1, chemin)
                    chemin.pop()

        resultat = []
        backtrack(0, [])
        return resultat


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert solution.partition("a") == [["a"]]
    assert solution.partition("abc") == [["a", "b", "c"]]
    assert solution.partition("bb") == [["b", "b"], ["bb"]]
