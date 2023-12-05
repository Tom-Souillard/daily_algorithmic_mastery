class Solution:
    def numberOfMatches(self, n: int) -> int:
        """
        Calculate the total number of matches in a tournament.

        Args:
        n (int): The number of teams in the tournament.

        Returns:
        int: The total number of matches played until a winner is decided.

        This function computes the total number of matches based on the number of teams.
        The total number of matches is always one less than the number of teams, as each
        match eliminates one team from the tournament.
        """
        return n - 1
