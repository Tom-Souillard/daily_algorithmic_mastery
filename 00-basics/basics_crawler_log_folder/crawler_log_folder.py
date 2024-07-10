from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        Calculate the minimum number of operations needed to return to the main folder
        after performing a series of change folder operations.

        Args:
            logs (List[str]): A list of strings representing the operations performed.

        Returns:
            int: The minimum number of operations needed to return to the main folder.
        """
        niveau = 0
        for operation in logs:
            if operation == "../":
                if niveau > 0:
                    niveau -= 1
            elif operation != "./":
                niveau += 1
        return niveau

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minOperations(["d1/","d2/","../","d21/","./"]) == 2
    assert solution.minOperations(["d1/","d2/","./","d3/","../","d31/"]) == 3
    assert solution.minOperations(["d1/","../","../","../"]) == 0
    print("All tests passed.")
