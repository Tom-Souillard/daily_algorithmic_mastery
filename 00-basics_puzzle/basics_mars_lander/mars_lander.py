surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    power_index = 0

    rotate_index = 0
    if abs(v_speed) >= 20:
        power_index = 4

    if abs(h_speed) >= 40:
        power_index = 4
    print(rotate_index, power_index)
