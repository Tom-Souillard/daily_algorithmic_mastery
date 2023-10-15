import sys

l = int(input())
h = int(input())
t = input()
print(t, file=sys.stderr, flush=True)
ascii_dict = {}

for i in range(h):
    row = input()
    for j in range(26):
        letter = chr(ord('A') + j)
        if letter not in ascii_dict:
            ascii_dict[letter] = ""
        ascii_dict[letter] += row[j * l:(j + 1) * l]
    if '?' not in ascii_dict:
        ascii_dict['?'] = ""
    ascii_dict['?'] += row[26 * l:(26 + 1) * l]

for i in range(h):
    line = ""
    for char in t:
        if char.isalpha():
            char = char.upper()
            line += ascii_dict[char][i * l:(i + 1) * l]
        else:
            line += ascii_dict['?'][i * l:(i + 1) * l]
    print(line)

