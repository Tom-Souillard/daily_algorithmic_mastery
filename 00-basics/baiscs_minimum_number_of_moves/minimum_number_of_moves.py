class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        """
        Returns the minimum number of moves required to seat all students.

        Args:
        seats (List[int]): The positions of the seats.
        students (List[int]): The positions of the students.

        Returns:
        int: The minimum number of moves.
        """
        seats.sort()
        students.sort()
        return sum(abs(siege - etudiant) for siege, etudiant in zip(seats, students))


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minMovesToSeat([3, 1, 5], [2, 7, 4]) == 4
    assert solution.minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6]) == 7
    assert solution.minMovesToSeat([2, 2, 6, 6], [1, 3, 2, 6]) == 4
    assert solution.minMovesToSeat([1, 2, 3], [1, 2, 3]) == 0
    print("All tests passed.")
