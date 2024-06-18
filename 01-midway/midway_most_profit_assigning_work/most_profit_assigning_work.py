class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        """
        This function calculates the maximum profit achievable by assigning workers to jobs based on their abilities.

        Args:
            difficulty (List[int]): List of job difficulties.
            profit (List[int]): List of job profits.
            worker (List[int]): List of worker abilities.

        Returns:
            int: Maximum profit achievable.
        """
        travaux = sorted(zip(difficulty, profit))
        travailleurs = sorted(worker)
        max_profit = 0
        i = 0
        best_profit = 0

        for capacité in travailleurs:
            while i < len(travaux) and capacité >= travaux[i][0]:
                best_profit = max(best_profit, travaux[i][1])
                i += 1
            max_profit += best_profit

        return max_profit


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]) == 100
    assert solution.maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]) == 0
    assert solution.maxProfitAssignment([1, 2, 3, 4], [10, 20, 30, 40], [5, 5, 5, 5]) == 160
    print("All tests passed.")
