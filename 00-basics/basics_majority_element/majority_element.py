def majorityElement(nums):
    """
    Finds the majority element in an array. The majority element is the one that appears more than floor(n/2) times.

    Args:
    nums: List[int] - A list of integers representing the input array.

    Returns:
    int - The majority element in the array.

    Example:
    >>> majorityElement([3,2,3])
    3
    >>> majorityElement([2,2,1,1,1,2,2])
    2
    """
    compteur = 0
    candidat = None

    for num in nums:
        if compteur == 0:
            candidat = num
        compteur += (1 if num == candidat else -1)

    return candidat
