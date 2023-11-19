class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        """
        Calculates the minimum number of reduction operations needed to make all
        elements in the array equal. Each operation reduces the largest element
        to the next largest element in the array.

        Args:
        nums (List[int]): The input array of integers.

        Returns:
        int: The minimum number of operations required to make all elements equal.
        """
        triNums = sorted(nums)  # Trier les nombres en ordre croissant.
        operations = 0
        differents = 0  # Compter le nombre de valeurs différentes.

        # Parcourir le tableau trié et compter les opérations nécessaires.
        for i in range(1, len(triNums)):
            if triNums[i] != triNums[i - 1]:
                differents += 1
            operations += differents

        return operations
