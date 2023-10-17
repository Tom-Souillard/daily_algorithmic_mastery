import sys
import math

largeur = int(input())
hauteur = int(input())

grille = []
for i in range(hauteur):
    ligne = input()
    grille.append(list(ligne))

for y1 in range(hauteur):
    for x1 in range(largeur):
        if grille[y1][x1] == '0':
            x2, y2, x3, y3 = -1, -1, -1, -1
            for xn in range(x1 + 1, largeur):
                if grille[y1][xn] == '0':
                    x2, y2 = xn, y1
                    break

            for yn in range(y1 + 1, hauteur):
                if grille[yn][x1] == '0':
                    x3, y3 = x1, yn
                    break

            print(f"{x1} {y1} {x2} {y2} {x3} {y3}")
