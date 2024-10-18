import sys

MIN_INT = -1 * sys.maxsize
n = int(input())

arr = []
for i in range(n):
    l = list(map(int, input().split()))
    arr.append(l)

max_val = MIN_INT
# 1*3 격자로 탐색 진행하기
for i in range(n):
    for j in range(n-2):
        max_val = max(max_val, arr[i][j]+arr[i][j+1]+arr[i][j+2])

print(max_val)