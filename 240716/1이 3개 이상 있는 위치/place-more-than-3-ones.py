n = int(input())

mapp=[]
for i in range(n):
    arr = list(map(int, input().split()))
    mapp.append(arr)


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0
for i in range(n):
    for j in range(n):
        y = i
        x = j
        cnt = 0

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if mapp[ny][nx] == 1:
                cnt += 1

        if cnt >= 3:
            answer +=1
print(answer)