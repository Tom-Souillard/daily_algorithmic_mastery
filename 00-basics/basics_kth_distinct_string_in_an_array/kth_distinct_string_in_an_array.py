from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        """Finds the kth distinct string in an array of strings.

        Args:
            arr: List of strings.
            k: The k-th position to find the distinct string.

        Returns:
            The k-th distinct string if it exists, otherwise an empty string.
        """
        freq = {}
        for chaine in arr:
            if chaine in freq:
                freq[chaine] += 1
            else:
                freq[chaine] = 1
        distincts = [chaine for chaine in arr if freq[chaine] == 1]
        return distincts[k-1] if k <= len(distincts) else ""

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.kthDistinct(["d", "b", "c", "b", "c", "a"], 2) == "a"
    assert solution.kthDistinct(["aaa", "aa", "a"], 1) == "aaa"
    assert solution.kthDistinct(["a", "b", "a"], 3) == ""
    assert solution.kthDistinct(["a", "a", "b", "c", "d", "c", "e"], 2) == "d"
    assert solution.kthDistinct([], 1) == ""
    print("All tests passed.")
