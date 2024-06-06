from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Determines if the hand can be rearranged into groups of consecutive cards.

        Args:
            hand (list[int]): List of integers representing the hand of cards.
            groupSize (int): Size of each group of consecutive cards.

        Returns:
            bool: True if the hand can be rearranged into groups, False otherwise.
        """
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        sorted_hand = sorted(hand)

        for card in sorted_hand:
            if count[card] > 0:
                for i in range(groupSize):
                    if count[card + i] > 0:
                        count[card + i] -= 1
                    else:
                        return False
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) == True
    assert solution.isNStraightHand([1, 2, 3, 4, 5], 4) == False
    assert solution.isNStraightHand([1, 2, 3, 4, 5, 6], 2) == True
    assert solution.isNStraightHand([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == True
    assert solution.isNStraightHand([1, 2, 3, 6, 7, 8, 10, 11, 12], 3) == True
    assert solution.isNStraightHand([8, 10, 12], 3) == False
    print("All tests passed.")