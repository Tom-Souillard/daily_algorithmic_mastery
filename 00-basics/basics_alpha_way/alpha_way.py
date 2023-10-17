def dfs(grille, x, y, alphabet, indice, resultat):
    n = len(grille)
    if indice == len(alphabet):
        return True
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if grille[nx][ny] == alphabet[indice]:
                resultat[nx][ny] = alphabet[indice]
                if dfs(grille, nx, ny, alphabet, indice + 1, resultat):
                    return True
    return False

n = int(input())
grille = [list(input()) for _ in range(n)]
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(n):
    for j in range(n):
        if grille[i][j] == 'a':
            temp_resultat = [['-' for _ in range(n)] for _ in range(n)]
            temp_resultat[i][j] = 'a'
            if dfs(grille, i, j, alphabet, 1, temp_resultat):
                for ligne in temp_resultat:
                    print("".join(ligne))
                exit(0)

