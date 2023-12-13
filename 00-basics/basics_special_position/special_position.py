def numSpecial(mat):
    """
    Counts the number of special positions in a binary matrix.

    A position (i, j) is special if mat[i][j] is 1 and all other elements in row i and column j are 0.

    Args:
    mat (List[List[int]]): A binary matrix.

    Returns:
    int: Number of special positions in the matrix.

    Example:
        Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
        Output: 1
    """
    compteLignes = [0] * len(mat)
    compteColonnes = [0] * len(mat[0])

    # Compter les 1 dans chaque ligne et colonne
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                compteLignes[i] += 1
                compteColonnes[j] += 1

    # Compter les positions spéciales
    positionsSpeciales = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1 and compteLignes[i] == 1 and compteColonnes[j] == 1:
                positionsSpeciales += 1

    return positionsSpeciales
