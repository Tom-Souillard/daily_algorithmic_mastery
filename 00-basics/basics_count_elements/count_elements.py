from typing import List


def maxFrequencyElements(nums: List[int]) -> int:
    """
    Counts the total frequency of elements in the array such that these elements have the maximum frequency.

    Args:
    nums: A list of positive integers.

    Returns:
    An integer representing the total number of elements with maximum frequency.
    """
    # Comptage des fréquences de chaque élément
    frequences = {}
    for num in nums:
        if num in frequences:
            frequences[num] += 1
        else:
            frequences[num] = 1

    # Trouver la fréquence maximale
    frequence_max = max(frequences.values())

    # Compter le nombre total d'éléments ayant la fréquence maximale
    total = sum(frequence == frequence_max for frequence in frequences.values())

    return total * frequence_max

# Vous pouvez tester la fonction avec un exemple
# print(maxFrequencyElements([1,2,2,3,1,4])) # Devrait afficher 4
