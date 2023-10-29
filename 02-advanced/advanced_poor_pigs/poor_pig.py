import math


class Solution:
    def poorPigs(self, seaux: int, minutesPourMourir: int, minutesPourTester: int) -> int:
        """
        Determine the minimum number of pigs needed to identify the poisonous bucket.

        Parameters:
        - seaux (int): The number of buckets, one of which is poisonous.
        - minutesPourMourir (int): The number of minutes it takes for a pig to die after consuming the poison.
        - minutesPourTester (int): The total number of minutes available to run the tests.

        Returns:
        int: The minimum number of pigs needed to identify the poisonous bucket within the given time.
        """
        toursDeTest = minutesPourTester // minutesPourMourir
        cochons = 0
        while (toursDeTest + 1) ** cochons < seaux:
            cochons += 1
        return cochons
