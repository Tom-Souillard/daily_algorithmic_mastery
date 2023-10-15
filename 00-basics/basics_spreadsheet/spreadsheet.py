import functools

cellules = [input().split() for _ in range(int(input()))]


@functools.lru_cache()
def valeur(operation, arg_1, arg_2):
    def ref_or_valeur(arg):
        if arg.startswith('$'):
            return valeur(*cellules[int(arg[1:])])
        else:
            return int(arg)

    if operation == 'VALUE':
        return ref_or_valeur(arg_1)
    if operation == 'ADD':
        return ref_or_valeur(arg_1) + ref_or_valeur(arg_2)
    if operation == 'SUB':
        return ref_or_valeur(arg_1) - ref_or_valeur(arg_2)
    if operation == 'MULT':
        return ref_or_valeur(arg_1) * ref_or_valeur(arg_2)


for cellule in cellules:
    print(valeur(*cellule))
