class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Generates the nth term of the count-and-say sequence.

        Args:
        n: An integer representing the position in the count-and-say sequence.

        Returns:
        A string representing the nth term of the count-and-say sequence.
        """
        if n == 1:
            return "1"
        precedent = self.countAndSay(n - 1)
        resultat = ""
        compteur = 1
        for i in range(1, len(precedent)):
            if precedent[i] == precedent[i - 1]:
                compteur += 1
            else:
                resultat += str(compteur) + precedent[i - 1]
                compteur = 1
        resultat += str(compteur) + precedent[-1]
        return resultat

# Partie test
if __name__ == "__main__":
    solution = Solution()
    assert solution.countAndSay(1) == "1", "cas n=1"
    assert solution.countAndSay(2) == "11", "cas n=2"
    assert solution.countAndSay(3) == "21", "cas n=3"
    assert solution.countAndSay(4) == "1211", "cas n=4"
    assert solution.countAndSay(5) == "111221", "cas n=5"
