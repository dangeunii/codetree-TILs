str = input()
str = list(str)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

dir = 3
x = 0
y = 0

for word in str:
    if word == "L":
        dir = (dir+1)%4
    elif word == "R":
        dir = (dir-1)%4
    else:
        x = x + dx[dir]
        y = y + dy[dir]

print(x, y)