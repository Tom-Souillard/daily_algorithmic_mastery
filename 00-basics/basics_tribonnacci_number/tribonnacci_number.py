class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Calculate the n-th number in the Tribonacci sequence.

        Args:
        n (int): The index of the Tribonacci number to retrieve.

        Returns:
        int: The n-th Tribonacci number.
        """
        if n < 2:
            return n
        if n == 2:
            return 1
        dernier, avant_dernier, avant_avant_dernier = 1, 1, 0
        for _ in range(3, n + 1):
            prochain = dernier + avant_dernier + avant_avant_dernier
            avant_avant_dernier, avant_dernier, dernier = avant_dernier, dernier, prochain
        return dernier

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.tribonacci(4) == 4, "Le cas de n=4 doit retourner 4"
    assert solution.tribonacci(25) == 1389537, "Le cas de n=25 doit retourner 1389537"
    assert solution.tribonacci(0) == 0, "Le cas de n=0 doit retourner 0"
    assert solution.tribonacci(1) == 1, "Le cas de n=1 doit retourner 1"
    assert solution.tribonacci(2) == 1, "Le cas de n=2 doit retourner 1"
    assert solution.tribonacci(3) == 2, "Le cas de n=3 doit retourner 2"
    print("Tous les tests passent.")
