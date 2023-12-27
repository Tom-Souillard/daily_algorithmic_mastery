class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        Calculate the minimum time required to make the rope colorful by removing
        consecutive balloons of the same color.

        Args:
        colors: A string representing the colors of the balloons on the rope.
        neededTime: A list of integers where neededTime[i] is the time to remove the ith balloon.

        Returns:
        int: The minimum total time to make the rope colorful by removing balloons.

        Time Complexity: O(n), where n is the length of the colors string.
        Space Complexity: O(1), constant space used.
        """
        tempsTotal = 0
        i = 0

        while i < len(colors):
            maxTime = neededTime[i]
            sumTime = neededTime[i]
            while i + 1 < len(colors) and colors[i] == colors[i + 1]:
                i += 1
                sumTime += neededTime[i]
                maxTime = max(maxTime, neededTime[i])

            tempsTotal += sumTime - maxTime
            i += 1

        return tempsTotal


# Example usage:
solution = Solution()
print(solution.minCost("abaac", [1, 2, 3, 4, 5]))  # Output: 3
