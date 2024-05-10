import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        """
        The function calculates the k-th smallest fraction from all possible fractions formed by elements of arr.

        Args:
            arr: A sorted list of integers containing 1 and unique prime numbers.
            k: An integer representing the k-th position.

        Returns:
            A list of two integers representing the k-th smallest fraction.
        """
        min_heap = []
        n = len(arr)
        for i in range(n - 1):
            for j in range(i + 1, n):
                heapq.heappush(min_heap, (arr[i] / arr[j], arr[i], arr[j]))

        while k > 1:
            heapq.heappop(min_heap)
            k -= 1

        _, numerateur, denominateur = heapq.heappop(min_heap)
        return [numerateur, denominateur]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.kthSmallestPrimeFraction([1, 2, 3, 5], 3) == [2, 5], "Test case 1 failed"
    assert solution.kthSmallestPrimeFraction([1, 7], 1) == [1, 7], "Test case 2 failed"