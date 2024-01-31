class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        This function takes a list of daily temperatures and returns a list where
        each element is the number of days until a warmer temperature. If no such
        day exists, the value is 0.

        Args:
        temperatures (List[int]): A list of integers representing daily temperatures.

        Returns:
        List[int]: A list of integers where each value represents the number of days
                   until a warmer temperature.

        """
        longueur = len(temperatures)
        reponse = [0] * longueur
        pile = []

        for index, temp in enumerate(temperatures):
            while pile and temp > temperatures[pile[-1]]:
                dernierIndex = pile.pop()
                reponse[dernierIndex] = index - dernierIndex
            pile.append(index)

        return reponse
