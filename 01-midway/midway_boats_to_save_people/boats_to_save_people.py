from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Given an array of integers representing the weights of people and a weight limit for boats,
        this function returns the minimum number of boats required to carry all people under the constraints
        that each boat can carry at most two people and the combined weight of these people cannot exceed the limit.

        Args:
        people: List[int] - A list of integers where each integer represents the weight of a person.
        limit: int - The maximum weight that each boat can carry.

        Returns:
        int - The minimum number of boats required.

        """
        people.sort()
        gauche = 0
        droite = len(people) - 1
        bateaux = 0
        while gauche <= droite:
            if people[gauche] + people[droite] <= limit:
                gauche += 1
            droite -= 1
            bateaux += 1
        return bateaux

# Test section
if __name__ == "__main__":
    sol = Solution()
    assert sol.numRescueBoats([1, 2], 3) == 1, "Test case 1 failed"
    assert sol.numRescueBoats([3, 2, 2, 1], 3) == 3, "Test case 2 failed"
    assert sol.numRescueBoats([3, 5, 3, 4], 5) == 4, "Test case 3 failed"
    assert sol.numRescueBoats([3, 3, 4, 5], 5) == 4, "New test case failed"
