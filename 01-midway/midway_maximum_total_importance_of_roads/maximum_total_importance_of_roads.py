class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        """
        Calculate the maximum total importance of all roads possible after assigning the values optimally.

        Args:
        n (int): The number of cities.
        roads (list[list[int]]): 2D integer array where each element is a list of two integers representing a bidirectional road between two cities.

        Returns:
        int: The maximum total importance of all roads.
        """
        from collections import defaultdict

        degres = defaultdict(int)
        for a, b in roads:
            degres[a] += 1
            degres[b] += 1

        degres_trie = sorted(degres.values(), reverse=True)
        importance_totale = 0

        for i, degre in enumerate(degres_trie):
            importance_totale += (n - i) * degre

        return importance_totale


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumImportance(5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]) == 43
    assert solution.maximumImportance(5, [[0, 3], [2, 4], [1, 3]]) == 20
    print("All tests passed.")
