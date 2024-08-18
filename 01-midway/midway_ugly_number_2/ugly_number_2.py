class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        Determines the nth number in a sequence where the prime factors
        are limited to 2, 3, and 5.

        Args:
            n (int): The position in the sequence to retrieve.

        Returns:
            int: The nth number in the sequence.
        """
        facteurs_deux = facteurs_trois = facteurs_cinq = 0
        seq = [1]
        while len(seq) < n:
            prochain = min(seq[facteurs_deux] * 2, seq[facteurs_trois] * 3, seq[facteurs_cinq] * 5)
            seq.append(prochain)
            if prochain == seq[facteurs_deux] * 2:
                facteurs_deux += 1
            if prochain == seq[facteurs_trois] * 3:
                facteurs_trois += 1
            if prochain == seq[facteurs_cinq] * 5:
                facteurs_cinq += 1
        return seq[-1]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.nthUglyNumber(10) == 12
    assert solution.nthUglyNumber(1) == 1
    assert solution.nthUglyNumber(15) == 24
    assert solution.nthUglyNumber(150) == 5832
    print("All tests passed.")
