message = input()


def conversion_binaire(mot_a_transformer):
    return bin(ord(mot_a_transformer))[2:].zfill(7)


def encodage(mot_binaire):
    compteur = 1
    encodage = ""
    if mot_binaire[0] == "1":
        encodage += "0 "
    else:
        encodage += "00 "

    num_bit = 1

    for bit in mot_binaire[1:]:

        if mot_binaire[num_bit] == mot_binaire[num_bit - 1]:
            compteur += 1
            num_bit += 1
        else:
            encodage += "0" * compteur + " "
            compteur = 1
            if mot_binaire[num_bit] == "1":
                encodage += "0 "

            else:
                encodage += "00 "
            num_bit += 1

    encodage += "0" * compteur
    return encodage


resultat = ''.join([conversion_binaire(char) for char in message])
print(encodage(resultat))