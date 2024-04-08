from typing import List
from collections import Counter

class Solution:
    def countStudents(self, eleves: List[int], sandwiches: List[int]) -> int:
        """
        Counts the number of students who cannot eat given their preferences and available sandwiches.

        Args:
        eleves: A list of integers representing student sandwich preferences.
        sandwiches: A list of integers representing the types of sandwiches in the stack.

        Returns:
        An integer representing the number of students unable to eat.
        """
        preferences = Counter(eleves)
        i = 0
        while i < len(sandwiches) and preferences[sandwiches[i]]:
            preferences[sandwiches[i]] -= 1
            i += 1
        return len(eleves) - i


# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    eleves1 = [1, 1, 0, 0]
    sandwiches1 = [0, 1, 0, 1]
    assert solution.countStudents(eleves1, sandwiches1) == 0, "Test case 1 failed"
    # Test case 2
    eleves2 = [1, 1, 1, 0, 0, 1]
    sandwiches2 = [1, 0, 0, 0, 1, 1]
    assert solution.countStudents(eleves2, sandwiches2) == 3, "Test case 2 failed"
    # Additional test case
    eleves3 = [0, 0, 1, 1]
    sandwiches3 = [1, 0, 0, 1]
    assert solution.countStudents(eleves3, sandwiches3) == 0, "Additional test case failed"
    print("All test cases passed.")
