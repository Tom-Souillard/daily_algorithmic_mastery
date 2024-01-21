class Solution:
    def rob(self, maisons: List[int]) -> int:
        """
        Calculate the maximum amount of money that can be robbed without alerting the police.

        Args:
        maisons (List[int]): A list of integers representing the amount of money in each house.

        Returns:
        int: The maximum amount of money that can be robbed.

        This function implements a dynamic programming approach to solve the problem, using
        two variables to keep track of the maximum amounts that can be robbed up to the
        current house, considering whether the current house is robbed or not.
        """
        if not maisons:
            return 0

        voler = 0  # Maximum amount if the current house is robbed
        ne_pas_voler = 0  # Maximum amount if the current house is not robbed

        for argent in maisons:
            temp = max(voler, ne_pas_voler)
            voler = ne_pas_voler + argent
            ne_pas_voler = temp

        return max(voler, ne_pas_voler)
