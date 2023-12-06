class Solution:
    def totalMoney(self, n: int) -> int:
        """
        Calculate the total money deposited in the Leetcode bank over 'n' days.

        The deposit starts with $1 on the first day and increases by $1 each day. Every
        Monday, the starting deposit amount increases by $1 compared to the previous Monday.

        Args:
        n (int): The number of days to calculate the total deposit.

        Returns:
        int: The total amount of money deposited over 'n' days.
        """
        semaines = n // 7
        jours_restants = n % 7
        gain_total = 0

        for semaine in range(semaines):
            gain_total += (28 + 7 * semaine)

        gain_total += sum(jour + semaines for jour in range(1, jours_restants + 1))

        return gain_total
