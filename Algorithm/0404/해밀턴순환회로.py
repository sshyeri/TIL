def perm(n, r, before, c):
    global ans, N
    if c >= ans: return
    if r >= N-1:
        c += cost[before][0]
        if ans > c: ans = c
        return
    if n >= N: return
    for i in range(1, N):
        if not chk[i] and cost[before][i]:
            if n == N - 2 and not cost[i][0]:continue
            chk[i] = 1
            perm(n+1, r+1, i, c + cost[before][i])
            chk[i] = 0

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
ans = 10000
chk = [0]*N
v=[0]*(N-1)
perm(0, 0, 0, 0)
print(ans)