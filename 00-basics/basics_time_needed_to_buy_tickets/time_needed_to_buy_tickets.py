from typing import List
import unittest


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        Calculate the time needed for a person at position k to buy tickets.

        Args:
        tickets: A list of integers representing the number of tickets each person wants to buy.
        k: The position of the person in the queue (0-indexed).

        Returns:
        The time taken for the person at position k to finish buying tickets.
        """
        temps = 0
        for i, billets in enumerate(tickets):
            if i <= k:
                temps += min(billets, tickets[k])
            else:
                temps += min(billets, tickets[k] - 1)
        return temps


# class TestTimeRequiredToBuy(unittest.TestCase):
#
#     def setUp(self):
#         self.solution = Solution()
#
#     def test_example_1(self):
#         self.assertEqual(self.solution.timeRequiredToBuy([2, 3, 2], 2), 6, "Le temps devrait être de 6 secondes.")
#
#     def test_example_2(self):
#         self.assertEqual(self.solution.timeRequiredToBuy([5, 1, 1, 1], 0), 8, "Le temps devrait être de 8 secondes.")
#
#     def test_additional_case(self):
#         self.assertEqual(self.solution.timeRequiredToBuy([3, 6, 3, 4], 2), 10, "Le temps devrait être de 10 secondes.")
#
# if __name__ == "__main__":
#     unittest.main()
