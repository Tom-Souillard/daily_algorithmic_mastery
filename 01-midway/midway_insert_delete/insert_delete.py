import random

class RandomizedSet:
    """
    This class implements a data structure that supports insertion, deletion,
    and fetching a random element in average O(1) time complexity.

    Attributes:
        val_to_index (dict): A dictionary mapping values to their indices in the array.
        values (list): An array storing the elements of the set.
    """

    def __init__(self):
        """
        Initializes a new instance of the RandomizedSet class.
        """
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value into the set.

        Args:
            val (int): The value to be inserted.

        Returns:
            bool: True if the value was not present and was inserted successfully, False otherwise.
        """
        if val in self.val_to_index:
            return False

        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set.

        Args:
            val (int): The value to be removed.

        Returns:
            bool: True if the value was present and was removed successfully, False otherwise.
        """
        if val not in self.val_to_index:
            return False

        # Move the last element to the position of the element to be removed
        last_val = self.values[-1]
        idx_to_remove = self.val_to_index[val]
        self.values[idx_to_remove] = last_val
        self.val_to_index[last_val] = idx_to_remove

        # Remove the last element
        self.values.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:
        """
        Returns a random element from the set.

        Returns:
            int: A random element from the set.
        """
        return random.choice(self.values)

# Example usage
randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))  # True
print(randomizedSet.remove(2))  # False
print(randomizedSet.insert(2))  # True
print(randomizedSet.getRandom())  # 1 or 2
print(randomizedSet.remove(1))   # True
print(randomizedSet.insert(2))   # False
print(randomizedSet.getRandom()) # 2
