class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        """
        Calculate the minimum cost required to hire k workers under specific rules.

        Args:
        quality (List[int]): List of the quality ratings of workers.
        wage (List[int]): List of the minimum wage expectations of workers.
        k (int): Number of workers to hire.

        Returns:
        float: The minimum cost to hire k workers.
        """
        from heapq import heappop, heappush

        travailleurs = sorted((w / q, q, w) for q, w in zip(quality, wage))
        cout_total = float('inf')
        qualite_totale = 0
        max_heap = []

        for ratio, qualite, salaire in travailleurs:
            heappush(max_heap, -qualite)
            qualite_totale += qualite
            if len(max_heap) > k:
                qualite_totale += heappop(max_heap)
            if len(max_heap) == k:
                cout_total = min(cout_total, ratio * qualite_totale)

        return cout_total


# Test cases
sol = Solution()
assert abs(sol.mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2) - 105.00000) <= 10 ** -5
assert abs(sol.mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3) - 30.66667) <= 10 ** -5
assert abs(sol.mincostToHireWorkers([4, 4, 4, 4], [100, 100, 100, 100], 2) - 200.0) <= 10 ** -5
