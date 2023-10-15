import sys
import math

n = int(input())
q = int(input())


dico_mime = {}
for i in range(n):
    ext, mt = input().split()
    dico_mime[ext.lower()] = mt

for i in range(q):
    fname = input()
    index_point = fname.rfind(".")

    if index_point != -1:
        extension = fname[index_point+1:].lower()
        print(dico_mime.get(extension,"UNKNOWN"))
    else:
        print("UNKNOWN")

