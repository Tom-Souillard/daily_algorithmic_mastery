class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        """
        This function computes the maximum distance between any two elements
        from different arrays within a list of sorted arrays.

        Args:
            arrays: A list of sorted integer arrays.

        Returns:
            The maximum absolute difference between two elements
            from two different arrays.
        """
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            max_distance = max(max_distance, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0]))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])

        return max_distance


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]) == 4
    assert solution.maxDistance([[1], [1]]) == 0
    assert solution.maxDistance([[1, 4, 7], [2, 6, 8], [3, 5, 9]]) == 8
    assert solution.maxDistance([[10, 20, 30], [5, 15, 25], [1, 2, 3]]) == 29
    print("All tests passed.")
