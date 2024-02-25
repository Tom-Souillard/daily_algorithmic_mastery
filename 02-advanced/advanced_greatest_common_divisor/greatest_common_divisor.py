from typing import List
from math import gcd
from collections import defaultdict


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        """
        Determines if it's possible to traverse between all pairs of indices in the given array such that
        for any two indices i and j, a path exists if gcd(nums[i], nums[j]) > 1.

        Args:
        nums: A list of integers representing the array to traverse.

        Returns:
        A boolean indicating whether it's possible to traverse between all pairs of indices under the given condition.
        """

        def trouverRacine(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(x, y):
            racineX = trouverRacine(x)
            racineY = trouverRacine(y)
            if racineX != racineY:
                parent[racineY] = racineX

        n = len(nums)
        parent = list(range(n))
        premier = defaultdict(list)

        for i, val in enumerate(nums):
            d = 2
            while d * d <= val:
                if val % d == 0:
                    while val % d == 0:
                        val //= d
                    premier[d].append(i)
                d += 1
            if val > 1:
                premier[val].append(i)

        for indices in premier.values():
            for i in range(len(indices) - 1):
                union(indices[i], indices[i + 1])

        racine = trouverRacine(0)
        for i in range(1, n):
            if trouverRacine(i) != racine:
                return False

        return True
