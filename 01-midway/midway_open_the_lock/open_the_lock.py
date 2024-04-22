from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        This function takes a list of deadends and a target combination, and determines the minimum number of moves
        required to reach the target from the starting combination "0000". If the target or initial state is blocked
        by a deadend, or if there is no possible way to reach the target due to deadends, the function returns -1.

        Args:
        deadends (List[str]): A list of strings representing the combinations that, once reached, prevent further movement.
        target (str): The target lock combination to reach from the starting combination "0000".

        Returns:
        int: The minimum number of moves needed to reach the target combination from "0000", or -1 if it is not possible.
        """
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0

        start_set = set(["0000"])
        end_set = set([target])
        visited = set(deadends)
        depth = 0

        def get_neighbors(state):
            neighbors = []
            for i in range(4):
                current_digit = int(state[i])
                for move in [-1, 1]:
                    new_digit = (current_digit + move) % 10
                    new_state = state[:i] + str(new_digit) + state[i + 1:]
                    neighbors.append(new_state)
            return neighbors

        while start_set and end_set:
            if len(start_set) > len(end_set):
                start_set, end_set = end_set, start_set

            temp = set()

            for state in start_set:
                for neighbor in get_neighbors(state):
                    if neighbor in end_set:
                        return depth + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        temp.add(neighbor)

            start_set = temp
            depth += 1

        return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6
    assert solution.openLock(["8888"], "0009") == 1
    assert solution.openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888") == -1
