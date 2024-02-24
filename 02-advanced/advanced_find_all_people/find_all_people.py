class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """
        Finds all people who know the secret after all meetings have taken place.

        Args:
        n: An integer indicating the total number of people.
        meetings: A list of lists where each sublist contains two people and the meeting time.
        firstPerson: An integer indicating the person who initially knows the secret apart from person 0.

        Returns:
        A list of integers representing all the people who know the secret.

        The function simulates the process of sharing secrets through meetings, using a priority queue
        to process meetings in chronological order and union-find to manage groupings of people who know
        the secret.
        """
        ensemble_connu = set([0, firstPerson])

        reunions_triees = []
        meetings.sort(key=lambda x: x[2])

        temps_vu = set()

        for reunion in meetings:
            if reunion[2] not in temps_vu:
                temps_vu.add(reunion[2])
                reunions_triees.append([])
            reunions_triees[-1].append((reunion[0], reunion[1]))

        for groupe_reunion in reunions_triees:
            personnes_connaissant_secret = set()
            graphe = defaultdict(list)

            for p1, p2 in groupe_reunion:
                graphe[p1].append(p2)
                graphe[p2].append(p1)
                if p1 in ensemble_connu:
                    personnes_connaissant_secret.add(p1)
                if p2 in ensemble_connu:
                    personnes_connaissant_secret.add(p2)

            file_attente = deque((personnes_connaissant_secret))

            while file_attente:
                actuel = file_attente.popleft()
                ensemble_connu.add(actuel)
                for voisin in graphe[actuel]:
                    if voisin not in ensemble_connu:
                        ensemble_connu.add(voisin)
                        file_attente.append(voisin)

        return list(ensemble_connu)