from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        Given an integer array 'deck', simulates revealing cards in increasing order. The function
        reorders the deck such that when cards are revealed following a specific pattern
        (reveal the top card, then put the next top card at the bottom, repeat), the revealed cards
        are in increasing order.

        Args:
        deck: List[int] representing the integers on each card in the deck.

        Returns:
        List[int]: The re-ordered deck.
        """
        deck.sort()
        reponse = collections.deque()
        for carte in reversed(deck):
            if reponse:
                reponse.appendleft(reponse.pop())
            reponse.appendleft(carte)
        return list(reponse)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    deck = [17, 13, 11, 2, 3, 5, 7]
    print(solution.deckRevealedIncreasing(deck))  # Output: [2,13,3,11,5,17,7]
    deck = [1, 1000]
    print(solution.deckRevealedIncreasing(deck))  # Output: [1,1000]
    deck = [3, 6, 1, 17, 28, 14, 12]
    print(solution.deckRevealedIncreasing(deck))  # Output attendu: [1,14,3,17,6,28,12]