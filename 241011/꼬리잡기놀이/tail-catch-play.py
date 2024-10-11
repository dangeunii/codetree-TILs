from collections import deque
## 구현해야 할 기능
## [1] 예술성 점수 구하기 - bfs로
## [1-1] pic 내에 들어있는 숫자 종류, 그룹별 좌표 구하기
## [1-2] 예술성 = (a그룹 칸 수 + b 그룹 칸수) * 그룹 a 숫자 * 그룹 b 숫자 * a와 b가 맞닿아있는 변의 수(강의에서는 조합에서 서로 인접하다고 판정되면 이 앞까지의 점수를 누적해서 더하는 것으로 구함!)
## [2] 십자모양 반시계 방향 90도 회전
## [3] N//2 * N//2 배열 시계 방향 90도 회전
## [4] 이 모든건 3번 반복 후 총합

# 입력받는 값
# n : n개의 줄
# pic : 초기 그림(숫자 배열)

n = int(input())
pic = []
for row in range(n):
    pic_r = list(map(int, input().split()))
    pic.append(pic_r)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
m = n //2

## [1] 그룹을 계산하고 그룹별 예술성 구하기
## 그룹을 구한다 -> dfs
num = 0
cnt = 0
isVisited = [[0] * n for _ in range(n)]
answer = 0
n_pic = [[0] * n for _ in range(n)]

def rotate_90(sy, sx, length):
    global pic, n_pic

    for y in range(sy, sy+length):
        for x in range(sx, sx+length):
            # 1. (0,0)으로 평행이동
            oy = y - sy
            ox = x - sx

            # 2. rotate
            ry , rx = ox, length - oy -1

            # 3. 적용하기
            n_pic[ry + sy][rx + sx] = pic[y][x]

    for y in range(sy, sy+length):
        for x in range(sx, sx + length):
            pic[y][x] = n_pic[y][x]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    isVisited[y][x] = 1
    groups[-1].add((y,x))

    while q:
        (cy,cx) = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<= ny < n and 0 <= nx < n and isVisited[ny][nx] == 0 and pic[ny][nx] == pic[y][x]:
                q.append((ny,nx))
                isVisited[ny][nx] = 1
                groups[-1].add((ny,nx))


for k in range(4):

    for y in range(n):
        for x in range(n):
            isVisited[y][x] = 0

    nums = []
    groups = []

    ## [1] 예술성 점수 구하기
    ## [1-1] bfs를 통해서 group, num 구하기
    for x in range(n):
        for y in range(n):
            if isVisited[y][x] == 0:
                nums.append(pic[y][x])
                groups.append(set())
                bfs(y,x)

    #print(groups)
    ## [1-2] 예술성 점수 = (a그룹 칸 수 + b 그룹 칸수) * 그룹 a 숫자 * 그룹 b 숫자 * a와 b가 맞닿아있는 변의 수(강의에서는 조합에서 서로 인접하다고 판정되면 이 앞까지의 점수를 누적해서 더하는 것으로 구함!)
    cnt = len(nums)
    point = 0
    for i in range(0,cnt-1):
        for j in range(i+1, cnt):
            point = (len(groups[i])+len(groups[j])) * nums[i] * nums[j]
            for (si, sj) in groups[i]:
                for l in range(4):
                    ni = si + dy[l]
                    nj = sj + dx[l]
                    if (ni, nj) in groups[j]:
                        answer += point
    #print("answer : ", answer)
    if k == 3:
        break

    #print(pic)
    ## [2] 회전하기 - 3번의 회전
    ## [2-1] 십자가 모양의 회전
    for a in range(n):
        n_pic[m][a] = pic[a][m]
        n_pic[a][m] = pic[m][n-1-a]

    rotate_90(0,0,m)
    rotate_90(0,m+1, m)
    rotate_90(m+1, 0, m)
    rotate_90(m+1, m+1, m)
    for i in range(n):
        for j in range(n):
            pic[i][j] = n_pic[i][j]

print(answer)