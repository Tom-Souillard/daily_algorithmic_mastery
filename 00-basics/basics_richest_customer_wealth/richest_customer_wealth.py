class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        """
        Calculate the maximum sum of sublists.

        Args:
            accounts (list[list[int]]): A list where each element is a list of integers.

        Returns:
            int: The maximum sum obtained by summing the integers in any single sublist.
        """
        return max([sum(customer) for customer in accounts])
        # return max(map(sum, accounts))


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
    assert solution.maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
    assert solution.maximumWealth([[10, 20, 30], [5, 5, 5], [15, 15, 10]]) == 60
    assert solution.maximumWealth([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]) == 12
    print("All tests passed.")