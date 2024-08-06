order = list(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

y = 0
x = 0
dir = 0
cnt = 0

def turn_right():
    global cnt, dir

    dir = (dir+1)%4
    cnt += 1

def turn_left():
    global cnt, dir

    dir = (dir-1)%4
    cnt += 1

def go():
    global dy, dx, cnt, y,x, dir

    y += dy[dir]
    x += dx[dir]

    cnt += 1

for i in order:
    if i == "L":
        turn_left()
    elif i == "R":
        turn_right()
    elif i == "F":
        go()
    
    if y == 0 and x == 0:
        print(cnt)
        break