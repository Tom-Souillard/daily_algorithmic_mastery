import sys
from queue import Queue

n, l, e = map(int, input().split())

liens = {}
for i in range(l):
    n1, n2 = map(int, input().split())
    if n1 not in liens:
        liens[n1] = []
    if n2 not in liens:
        liens[n2] = []
    liens[n1].append(n2)
    liens[n2].append(n1)

sortie = set()
for _ in range(e):
    noeud_sortie = int(input())
    sortie.add(noeud_sortie)

while True:
    position_bot = int(input())
    liste_verification = Queue()
    liste_verification.put(position_bot)
    visite = set()
    parent = {}
    trouve = False
    print(f"Position du bot = {position_bot}", file=sys.stderr, flush=True)
    print(f"Noeud voisin du bot = {liens[position_bot]}", file=sys.stderr, flush=True)

    while not liste_verification.empty():
        noeud_a_verifier = liste_verification.get()
        for noeud_voisin in liens[noeud_a_verifier]:
            if noeud_voisin not in visite:
                visite.add(noeud_voisin)
                parent[noeud_voisin] = noeud_a_verifier
                liste_verification.put(noeud_voisin)
                if noeud_voisin in sortie:
                    trouve = True
                    break
        if trouve == True:
            break

    if trouve == True:
        if parent[noeud_voisin] != position_bot:
            noeud_courant = parent[noeud_voisin]
        # Imprimer le lien à couper
        print(noeud_voisin, parent[noeud_voisin])