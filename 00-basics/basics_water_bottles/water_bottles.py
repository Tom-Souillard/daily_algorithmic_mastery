class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        Calculate the maximum number of water bottles you can drink given an initial
        number of full water bottles and a specific exchange rate for empty bottles.

        Args:
            numBottles (int): The initial number of full water bottles.
            numExchange (int): The number of empty bottles required to get one full bottle.

        Returns:
            int: The maximum number of water bottles that can be drunk.
        """
        total_drank = numBottles
        bouteilles_vides = numBottles

        while bouteilles_vides >= numExchange:
            nouvelles_bouteilles = bouteilles_vides // numExchange
            total_drank += nouvelles_bouteilles
            bouteilles_vides = nouvelles_bouteilles + (bouteilles_vides % numExchange)

        return total_drank


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.numWaterBottles(9, 3) == 13
    assert solution.numWaterBottles(15, 4) == 19
    assert solution.numWaterBottles(5, 5) == 6
    assert solution.numWaterBottles(2, 3) == 2
    print("All tests passed.")
