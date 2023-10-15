l = sorted([int(input()) for _ in range(int(input()))])
print(min((l[i+1] - l[i] for i in range(len(l) - 1))))