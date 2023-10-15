import re
import functools

def analyser_chaine():
    nom_tableau, borne_inf, valeurs = re.match(r'(\w+).(-?\d+).*=(.*)', input()).groups()
    return nom_tableau, {int(borne_inf) + i: int(v) for i, v in enumerate(valeurs.split())}

tableaux = dict(analyser_chaine() for _ in range(int(input())))
*noms, indice_final = input().replace(']', '').split('[')

print(functools.reduce(lambda n, s: tableaux[s][n], reversed(noms), int(indice_final)))
