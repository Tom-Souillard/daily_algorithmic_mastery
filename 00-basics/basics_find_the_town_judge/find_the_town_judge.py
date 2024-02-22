class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        """
        Determine the label of the town judge if one exists.

        This function identifies the town judge based on two properties:
        1. The town judge trusts nobody.
        2. Everybody else trusts the town judge.

        Args:
        n: An integer representing the number of people in the town.
        trust: A list of pairs [a, b] where a trusts b.

        Returns:
        The label of the town judge if one exists, otherwise -1.
        """
        if len(trust) < n - 1:
            return -1

        confiance = [0] * (n + 1)
        for a, b in trust:
            confiance[a] -= 1
            confiance[b] += 1

        for i in range(1, n + 1):
            if confiance[i] == n - 1:
                return i
        return -1
