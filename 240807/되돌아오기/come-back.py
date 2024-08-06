import sys

N = int(input())

y = 0
x = 0
cnt = 0

dy = [-1, 0 ,1, 0]
dx = [0, 1, 0, -1]

for i in range(N):
    dir, dis = map(str, input().split(" "))
    dis = int(dis)

    if dir == "N":
        for j in range(dis):
            y += dy[0]
            x += dx[0]
            cnt += 1
            if y == 0 and x == 0:
                print(cnt)
                break
    elif dir == "E":
        for j in range(dis):
            y += dy[1]
            x += dx[1]
            cnt += 1
            if y == 0 and x == 0:
                print(cnt)
                break
    elif dir == "S":
        for j in range(dis):
            y += dy[2]
            x += dx[2]
            cnt += 1
            if y == 0 and x == 0:
                print(cnt)
                break
    elif dir == "W":
        for j in range(dis):
            y += dy[3]
            x += dx[3]
            cnt += 1
            if y == 0 and x == 0:
                print(cnt)
                break
    if y == 0 and x == 0:
        break

if y != 0 or x != 0:
    print(-1)