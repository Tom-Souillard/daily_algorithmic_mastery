from collections import Counter

class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        """
        Calculate the minimum number of intervals required to complete all tasks
        with a given cooling time between the same type of tasks.

        Args:
        tasks: A list of strings representing tasks from A to Z.
        n: An integer representing the cooling interval between the same tasks.

        Returns:
        An integer representing the minimum number of intervals required to complete all tasks.

        The function uses a greedy approach to calculate the minimum intervals. It first counts
        the occurrences of each task, then finds the task with the maximum count. The idea is to
        arrange the tasks with maximum count as the framework and fill in the gaps with other tasks or idles.
        """
        compteur_taches = Counter(tasks)
        max_occurrences = max(compteur_taches.values())
        nb_taches_max = list(compteur_taches.values()).count(max_occurrences)
        intervalles = (max_occurrences - 1) * (n + 1) + nb_taches_max

        return max(intervalles, len(tasks))
