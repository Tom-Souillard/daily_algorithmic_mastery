from typing import List
from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        Calculate the maximum score of any valid set of words formed by using the given letters.

        Args:
            words (List[str]): List of words.
            letters (List[str]): List of single letters (might be repeating).
            score (List[int]): Score of every character a-z.

        Returns:
            int: Maximum score of any valid set of words.
        """

        def calculer_score(mot):
            return sum(score[ord(c) - ord('a')] for c in mot)

        def est_valide(mot, compteur_lettres):
            compteur_mot = Counter(mot)
            for lettre in compteur_mot:
                if compteur_mot[lettre] > compteur_lettres[lettre]:
                    return False
            return True

        def backtrack(index, compteur_lettres):
            if index == len(words):
                return 0
            max_score = backtrack(index + 1, compteur_lettres)
            mot = words[index]
            if est_valide(mot, compteur_lettres):
                for c in mot:
                    compteur_lettres[c] -= 1
                max_score = max(max_score, calculer_score(mot) + backtrack(index + 1, compteur_lettres))
                for c in mot:
                    compteur_lettres[c] += 1
            return max_score

        compteur_lettres = Counter(letters)
        return backtrack(0, compteur_lettres)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxScoreWords(["dog", "cat", "dad", "good"], ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                                 [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                  0]))  # Output: 23
    print(solution.maxScoreWords(["xxxz", "ax", "bx", "cx"], ["z", "a", "b", "c", "x", "x", "x"],
                                 [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0,
                                  10]))  # Output: 27
    print(solution.maxScoreWords(["leetcode"], ["l", "e", "t", "c", "o", "d"],
                                 [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                                  0]))  # Output: 0
    print(solution.maxScoreWords(["apple", "plea", "dog", "go"], ["a", "a", "e", "p", "p", "l", "o", "g", "d"],
                                 [1, 3, 3, 2, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                  1]))  # Output: 15
