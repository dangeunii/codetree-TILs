n,m = map(int,input().split())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def check(x,y):
    if x <0 or x>= n or y <0 or y >=m:
        return 1
    else:
        return 0

mapp = [[ 0 for row in range(n)]for col in range(m)]
visited = [[0 for row in range(n)]for col in range(m)]
dir = 0
x=0
y=0
visited[0][0] = 1
mapp[0][0] =1
for i in range(1,n*m):
    ny = y + dy[dir]
    nx = x + dx[dir]

    if check(nx,ny) or visited[ny][nx] ==1:
        dir = (dir+1) % 4
        ny = y + dy[dir]
        nx = x + dx[dir]
    
    mapp[ny][nx] = i+1
    visited[ny][nx] = 1
    y =ny
    x=nx
    
for i in range(n):
    num =mapp[i]
    print(' '.join(map(str, num)))