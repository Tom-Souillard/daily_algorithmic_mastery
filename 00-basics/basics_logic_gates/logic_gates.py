#Définir les fonctions pour chaque porte logique
def and_operation(a,b):
    return "-" if a == "-" and b == "-" else "_"

def or_operation(a,b):
    return "-" if a == "-" or b == "-" else "_"

def xor_operation(a,b):
    return "_" if (a == "-" and b == "-") or (a == "_" and b == "_") else "-"

def nand_operation(a,b):
    return "_" if a == "-" and b == "-" else "-"

def nor_operation(a,b):
    return "_" if a == "-" or b == "-" else "-"

def nxor_operation(a,b):
    return "-" if (a == "-" and b == "-") or (a == "_" and b == "_") else "_"

# Créer un dictionnaire pour stocker les signaux d'entrée
dic_sig_input = {}

n = int(input())
m = int(input())

# Lire les signaux d'entrée et les stocker dans le dictionnaire
for i in range(n):
    input_name, input_signal = input().split()
    dic_sig_input[input_name] = input_signal

# Stocker les instructions de sortie pour les traiter
liste_instruction = [input().split() for _ in range(m)]

# Traiter chaque instruction de sortie
for instruction in liste_instruction:
    output_name, _type, input_name_1, input_name_2 = instruction

    signal_sortie = ""
    signal_1 = dic_sig_input[input_name_1]
    signal_2 = dic_sig_input[input_name_2]

    # Choisir la porte logique appropriée et construire le signal de sortie
    for s1, s2 in zip(signal_1, signal_2):
        if _type == "AND":
            signal_sortie += and_operation(s1,s2)
        elif _type == "OR":
            signal_sortie += or_operation(s1,s2)
        elif _type == "XOR":
            signal_sortie += xor_operation(s1,s2)
        elif _type == "NAND":
            signal_sortie += nand_operation(s1,s2)
        elif _type == "NOR":
            signal_sortie += nor_operation(s1,s2)
        elif _type == "NXOR":
            signal_sortie += nxor_operation(s1,s2)

    # Afficher le nom du signal de sortie et le signal
    print(f"{output_name} {signal_sortie}")
