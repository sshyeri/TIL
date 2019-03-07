def apples(si, sj, ei, ej):
    cnt = 0
    for r in range(si, ei):
        for c in range(sj, ej):
            cnt+=arr[r][c]
    return cnt
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
CNT = 0
cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
for i in range(1, N):
    for j in range(1, N):
        cnt1 = apples(0, 0, i, j)
        cnt2 = apples(0, j, i, N)
        cnt3 = apples(i, 0, N, j)
        cnt4 = apples(i, j, N, N)
        if cnt1==cnt2==cnt3==cnt4:
            CNT+=1
if CNT==0: print(-1)
else: print(CNT)