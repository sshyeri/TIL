y, x = map(int, input().split())
mats = [list(map(int, input().split())) for _ in range(y)]

for mat in mats:
    for i in range(x):
        if not mat[i]: continue
        else:
            mat[i]+=mat[i-1]
for i in mats:
    print(*i)
