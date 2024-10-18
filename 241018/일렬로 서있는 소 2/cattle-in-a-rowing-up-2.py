n = int(input())

cows = list(map(int, input().split()))

cnt = 0

for i, cowi in enumerate(cows):
    for j in range(i+1, len(cows)):
        for k in range(j+1, len(cows)):
           if cowi <= cows[j] and cows[j] <= cows[k] :
            cnt += 1 

print(cnt)