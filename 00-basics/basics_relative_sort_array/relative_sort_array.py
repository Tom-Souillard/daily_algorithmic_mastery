class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        """
        Sort elements of arr1 based on the order of elements in arr2. Elements not in arr2 are placed at the end in ascending order.

        Args:
            arr1 (list[int]): The array to be sorted.
            arr2 (list[int]): The array that defines the sorting order.

        Returns:
            list[int]: The sorted array.
        """
        ordre = {valeur: index for index, valeur in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (ordre.get(x, len(arr2)), x))

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
    assert solution.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]) == [22,28,8,6,17,44]
    print("All tests passed.")
