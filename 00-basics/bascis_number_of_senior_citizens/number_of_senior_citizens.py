from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        """
        Counts the number of individuals older than 60 based on their details.

        Args:
            details (List[str]): A list of strings, each representing details of a passenger.

        Returns:
            int: The number of passengers older than 60.
        """
        return sum(1 for detail in details if int(detail[11:13]) > 60)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]) == 2
    assert solution.countSeniors(["1313579440F2036","2921522980M5644"]) == 0
    assert solution.countSeniors(["1234567890M6500","0987654321F6111"]) == 2
    print("All tests passed.")
