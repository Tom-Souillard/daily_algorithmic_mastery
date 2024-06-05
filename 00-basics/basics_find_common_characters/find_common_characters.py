from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        Given a list of words, returns a list of characters that appear in all words including duplicates.

        Args:
            words (List[str]): A list of words.

        Returns:
            List[str]: A list of common characters.
        """
        from collections import Counter

        compteur_min = Counter(words[0])
        for mot in words[1:]:
            compteur_min &= Counter(mot)

        return list(compteur_min.elements())


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.commonChars(["bella", "label", "roller"]) == ["e", "l", "l"]
    assert solution.commonChars(["cool", "lock", "cook"]) == ["c", "o"]
    assert solution.commonChars(["ab", "ba", "ab"]) == ["a", "b"]
    print("All tests passed.")
