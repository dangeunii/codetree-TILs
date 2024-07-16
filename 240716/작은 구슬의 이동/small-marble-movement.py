n,t = map(int, input().split())

r, c, d = map(str, input().split())
r = int(r)
c = int(c)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

y = r
x = c

if d == "U":
    dir = 2
elif d == "D":
    dir = 0
elif d == "R":
    dir = 1
elif d == "L":
    dir = 3

for i in range(t):
    ny = y + dy[dir]
    nx = x + dx[dir]

    if ny < 1 or ny > n or nx < 1 or nx > n:
        dir = (dir+2) %4
        continue
    
    y = ny
    x = nx

print(y,x)