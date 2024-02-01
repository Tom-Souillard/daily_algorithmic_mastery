from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        """
        Divide the given array into subarrays of size 3 where the max difference
        between elements is less than or equal to k.

        Args:
        nums: List of integers representing the array to divide.
        k: An integer representing the maximum allowable difference.

        Returns:
        A list of lists, where each sublist is of size 3 with differences
        between elements less than or equal to k.
        """
        nums.sort()
        result = []
        temp = []

        for number in nums:
            temp.append(number)
            if len(temp) == 3:
                if temp[-1] - temp[0] <= k:
                    result.append(temp)
                    temp = []
                else:
                    return []
        return result if not temp else []
