w, h, count_x, count_y = 10, 5, 2, 1
segments_x = [2, 5]
segments_y = [3]

# w, h, count_x, count_y = [int(i) for i in input().split()]
# measures_x = [int(i) for i in input().split()]
# measures_y = [int(i) for i in input().split()]

# Ajout des extrémités pour faciliter le traitement.
measures_x = [0] + measures_x + [w]
measures_y = [0] + measures_y + [h]

# Initialisation des tableaux dp pour stocker les distances entre les mesures
dp_x = [measures_x[i] - measures_x[i - 1] for i in range(1, len(measures_x))]
dp_y = [measures_y[i] - measures_y[i - 1] for i in range(1, len(measures_y))]

print("dp_x:", dp_x, file=sys.stderr, flush=True)
print("dp_y:", dp_y, file=sys.stderr, flush=True)

square_count = 0

# Pour chaque paire de distances dans dp_x et dp_y
for i in range(len(dp_x)):
    for j in range(len(dp_y)):

        # La taille du carré potentiel est le minimum des deux distances
        square_size = min(dp_x[i], dp_y[j])

        # On vérifie s'il est possible de former un carré de cette taille sans traverser d'autres mesures
        k = 1
        while k < square_size and i + k < len(dp_x) and j + k < len(dp_y) and dp_x[i + k] > 0 and dp_y[j + k] > 0:
            k += 1

        # Si la taille du carré est atteinte, on augmente le compteur
        if k == square_size:
            square_count += 1
            print(f"Square found of size {square_size} at x={measures_x[i]}, y={measures_y[j]}", file=sys.stderr,
                  flush=True)

print(square_count)
