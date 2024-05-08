from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        This function takes an array of unique scores for athletes in a competition
        and returns their ranks based on their scores.

        Args:
        score (List[int]): A list of integers representing the scores of each athlete.

        Returns:
        List[str]: A list of strings representing the rank of each athlete corresponding to their score.
        """
        trie = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        resultat = ["" for _ in score]
        for indice, (i, _) in enumerate(trie):
            if indice == 0:
                resultat[i] = "Gold Medal"
            elif indice == 1:
                resultat[i] = "Silver Medal"
            elif indice == 2:
                resultat[i] = "Bronze Medal"
            else:
                resultat[i] = str(indice + 1)
        return resultat


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.findRelativeRanks([5, 4, 3, 2, 1]) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    assert solution.findRelativeRanks([10, 3, 8, 9, 4]) == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]