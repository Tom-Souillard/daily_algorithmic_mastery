w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]
xmin, xmax, ymin, ymax, x, y = 0, w, 0, h, x0, y0

while True:
    bomb_dir = input()
    if "U" in bomb_dir:
        ymax = y
    if "D" in bomb_dir:
        ymin = y
    if "R" in bomb_dir:
        xmin = x
    if "L" in bomb_dir:
        xmax = x

    y = ymin + ((ymax - ymin)//2)
    x = xmin + ((xmax - xmin)//2)
    print(x,y)