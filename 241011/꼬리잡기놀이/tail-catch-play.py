from collections import deque

# 입력 구현
# n : n개 줄, m : 팀의 갯수, k : 라운드 수
# map에서 1 : 머리사람, 2: 중간 사람, 3: 꼬리 사람, 4 : 이동 경로 표시

dy = [-1, 0 , 1, 0]
dx = [0, 1, 0, -1]

n, m, k = map(int, input().split())
mapp = []

answer = 0

for i in range(n):
    m_r = list(map(int, input().split()))
    mapp.append(m_r)

v = [[0]*n for _ in range(n)]

# [1-1] team 구현하기
# team은 bfs를 이용하며, 머리를 찾는 순간 시작된다.
team_num = 5
teams = {}

def bfs(y,x,team_num):
    team = []
    q = deque()
    q.append((y,x))
    v[y][x] = 1
    ## team으로 좌표 추가
    team.append((y,x))
    mapp[y][x] = team_num

    while(q):
        (sy,sx) = q.popleft()
        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]
            # 범위 내, 미방문, 2쪽 or 출발지에서 온게 아니라면 3도 가능
            if 0<= ny < n and 0<= nx < n and v[ny][nx] == 0:
                if mapp[ny][nx] == 2 or ((sy,sx) != (y,x) and mapp[ny][nx] == 3):
                    q.append((ny,nx))
                    team.append((ny,nx))
                    mapp[ny][nx] = team_num
    teams[team_num] = team


for y in range(n):
    for x in range(n):
        if mapp[y][x] == 1 and v[y][x] == 0:
            bfs(y,x,team_num)
            team_num += 1

for turn in range(1,k+1):
    #print("turn : ", turn)
    ## [1-2] 팀 내에서 이동 구현하기
    ## 꼬리부터 한칸씩 앞으로 이동 구현하기
    ## 꼬리는 pop, 머리는 머리앞의 4 insert
    for team in teams.values():
        ## 꼬리 1칸 앞으로
        ey,ex = team.pop()
        eny, enx = team[-1][0:]
        mapp[eny][enx] = mapp[ey][ex]
        mapp[ey][ex] = 4

        ## 머리 1칸 앞으로
        sy,sx = team[0][0:]
        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]
            # 범위 내, 값이 4
            if 0 <= ny <n and 0 <= nx < n and mapp[ny][nx] == 4:
                team.insert(0,(ny,nx))
                mapp[ny][nx] = mapp[sy][sx]

    ##for i in range(n):
    ##    print(mapp[i])

    # [2] 공 쏘기
    # k : 1 ~ n : (k,i)
    # k : n+1 ~ 2n : (n-i,k-n)
    # k : 2n+1 ~ 3n : (3n-k,n-i)
    # k : 3n+1 ~ 4n : (i, 4n-k)
    #print(teams)
    point = 0
    if 1 <= turn <= n:
        for i in range(n):
            t = turn - 1
            if mapp[t][i] != 4 and mapp[t][i] != 0:
                ty , tx = t, i
                #print(ty,tx)
                #print(mapp[t][i])
                if (ty,tx) in teams[mapp[t][i]]:
                    idx = teams[mapp[t][i]].index((ty,tx))
                    #print("idx : ",idx)
                    point = (idx+1) **2

                    ## 해당 팀에서 공을 맞으면 순서 뒤집기!!
                    teams[mapp[t][i]].reverse()

                break
    elif n + 1 <= turn <= 2 * n:
        for i in range(n):
            # 일단 만나는 점이 있는지 찾기
            # team 번호
            if mapp[n-i-1][turn-n-1] != 4 and mapp[n-i-1][turn-n-1] != 0:
                #print(n-i-1, turn-n-1)
                team = mapp[n-i-1][turn-n-1]

                #print("team: " ,teams[team])

                # 그리고 그 해당 좌표의 index 찾아서 point 구하기
                if (n-i-1,turn-n-1) in teams[team]:
                    idx = teams[team].index(((n-i-1),(turn-n-1)))
                    #print(idx)
                    point = (idx+1) **2
                    ## 해당 팀의 머리 꼬리 변경
                    teams[team].reverse()
                #print("point: ", point)
                break
    elif 2 * n + 1 <= turn <= 3 * n:
        for i in range(n):
            if mapp[3*n - turn - 1][n-i-1] != 4 and mapp[3*n - turn - 1] [n-i-1] != 0:
               team = mapp[3*n-turn -1][n-i-1]
               if ((3*n - turn - 1),(n-i-1)) in teams[team]:
                   idx = teams[team].index((3*n - turn - 1),(n-i-1))
                   point = (idx+1) ** 2
                   teams[team].reverse()
            break

    elif 3 * n + 1 <= turn <= 4 * n:
        for i in range(n):
            if mapp[i][4*n -turn -1] != 4 and mapp[i][4*n -turn -1] != 0:
                team = mapp[i][4*n - turn -1]
                if (i, 4*n -turn-1) in teams[team]:
                    idx = teams[team].index(i,4*n -turn-1)
                    point = (idx+1) **2
                    teams[team].reverse()
            break
    answer += point

print(answer)