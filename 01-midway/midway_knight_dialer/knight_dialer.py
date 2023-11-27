class Solution:
    def knightDialer(self, n: int) -> int:
        """
        Calculates the number of distinct phone numbers of length n that can be dialed
        using a chess knight's movement on a phone keypad.

        Args:
        n (int): The length of the phone number to be dialed.

        Returns:
        int: The number of distinct phone numbers modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        mouvements = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        touches = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0],
                   5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3],
                   9: [2, 4], 0: [4, 6]}

        dp = [1] * 10

        for _ in range(n - 1):
            prochain_dp = [0] * 10
            for touche in range(10):
                for voisin in touches[touche]:
                    prochain_dp[voisin] += dp[touche]
                    prochain_dp[voisin] %= MOD
            dp = prochain_dp

        return sum(dp) % MOD
