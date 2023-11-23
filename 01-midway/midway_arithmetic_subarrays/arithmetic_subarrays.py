class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        Checks if subarrays of nums can be rearranged into arithmetic sequences.

        Args:
        nums (List[int]): The main array of integers.
        l (List[int]): The start indices of the subarrays.
        r (List[int]): The end indices of the subarrays.

        Returns:
        List[bool]: A list where each element indicates whether the corresponding subarray can be rearranged into an arithmetic sequence.
        """
        resultats = []
        for debut, fin in zip(l, r):
            sous_tableau = sorted(nums[debut:fin + 1])
            difference = sous_tableau[1] - sous_tableau[0]
            est_arithmetique = all(
                sous_tableau[i + 1] - sous_tableau[i] == difference for i in range(len(sous_tableau) - 1))
            resultats.append(est_arithmetique)
        return resultats
