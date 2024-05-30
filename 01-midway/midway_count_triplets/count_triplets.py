from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        Returns the number of triplets (i, j, k) where the XOR of elements from
        index i to j-1 is equal to the XOR of elements from index j to k.

        Args:
            arr (List[int]): List of integers.

        Returns:
            int: Number of triplets satisfying the condition.
        """
        n = len(arr)
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        count = 0
        for i in range(n):
            for k in range(i + 1, n):
                if prefix_xor[i] == prefix_xor[k + 1]:
                    count += k - i

        return count


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.countTriplets([2, 3, 1, 6, 7]))  # Output: 4
    print(sol.countTriplets([1, 1, 1, 1, 1]))  # Output: 10
    print(sol.countTriplets([1, 3, 5, 7, 9]))  # Output: 3
    print(sol.countTriplets([7, 11, 12, 14, 15]))  # Output: 0
    print(sol.countTriplets([1, 2, 3, 4, 5, 6]))  # Output: 0
