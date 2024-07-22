class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        """
        Sorts a list of names based on the corresponding heights in descending order.

        Args:
            names (list[str]): List of names.
            heights (list[int]): List of heights corresponding to the names.

        Returns:
            list[str]: List of names sorted by height in descending order.
        """
        personnes = list(zip(heights, names))
        personnes.sort(reverse=True, key=lambda x: x[0])
        return [nom for _, nom in personnes]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]) == ["Mary", "Emma", "John"]
    assert solution.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]) == ["Bob", "Alice", "Bob"]
    print("All tests passed.")
