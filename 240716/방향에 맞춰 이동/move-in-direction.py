n = int(input())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

y = 0
x = 0

for i in range(n):
    dir, num = map(str, input().split())
    num = int(num)
    if dir == "N":
        y += dy[0]*num
        x += dx[0]*num
    elif dir == "E":
        y += dy[1]*num
        x += dx[1]*num
    elif dir == "S":
        y += dy[2]*num
        x += dx[2]*num
    elif dir == "W":
        y += dy[3]*num
        x += dx[3]*num


print(x, y)