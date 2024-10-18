l = list(input())

cnt = 0
for i, ll in enumerate(l):
    if ll == "(":
        for j in range(i, len(l)):
            if l[j] == ")":
                cnt += 1

print(cnt)