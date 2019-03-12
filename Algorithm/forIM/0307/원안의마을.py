def center(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:
                return (i, j)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

d = 0

i, j = center(N)
for r in range(N):
    for c in range(N):
        if arr[r][c]==1:
            td = (i-r)**2 + (j-c)**2
            if td>d: d = td
d **=0.5
if round(d)<d: print(round(d+1))
else : print(round(d))