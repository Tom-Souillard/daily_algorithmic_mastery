def coder_decoder_chaine(chaine, rotors, decalage_initial, operation):
    resultat = []
    decalage_courant = decalage_initial
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if operation == 'ENCODE':
        for char in chaine:
            char_tmp = chr(((ord(char) - ord('A') + decalage_courant) % 26) + ord('A'))
            for rotor in rotors:
                char_tmp = rotor[ord(char_tmp) - ord('A')]
            resultat.append(char_tmp)
            decalage_courant += 1
    elif operation == 'DECODE':
        for char in chaine:
            for rotor in reversed(rotors):
                index = rotor.find(char)
                char = alphabet[index]
            resultat.append(alphabet[(alphabet.find(char)-decalage_courant + 26) % 26])
            decalage_courant += 1
    return ''.join(resultat)
operation = input()
decalage_initial = int(input())
rotors = [input() for _ in range(3)]
message = input()
print(coder_decoder_chaine(message, rotors, decalage_initial, operation))