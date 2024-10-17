import sys
INT_MAX = sys.maxsize
# 정렬을 해서 가운데 값을 고르면 되지 않을까?
# 예제만 봐도 그건 아님

n = int(input())
vals = list(map(int, input().split()))
min_val = INT_MAX

for idx,val in enumerate(vals):
    point = 0
    for idx2, val2 in enumerate(vals):
        point += abs(idx-idx2) * val2
    if min_val > point:
        min_val = point

print(min_val)