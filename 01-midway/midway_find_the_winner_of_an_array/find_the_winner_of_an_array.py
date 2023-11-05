from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        """
        Determine the winner of the array game.

        The game is played between the first two elements of the array, with the larger
        number winning the round and staying at the beginning of the array, while the
        smaller number moves to the end. The game ends when a number wins 'k' consecutive rounds.

        Args:
            arr: A list of distinct integers representing the initial state of the game.
            k: An integer representing the number of consecutive wins needed to end the game.

        Returns:
            An integer representing the number that wins the game by achieving 'k' consecutive wins.
        """
        gagnant_actuel = arr[0]
        compteur_victoires = 0

        for adversaire in arr[1:]:
            if gagnant_actuel > adversaire:
                compteur_victoires += 1
            else:
                gagnant_actuel = adversaire
                compteur_victoires = 1

            if compteur_victoires == k:
                return gagnant_actuel

        return max(gagnant_actuel, max(arr))
