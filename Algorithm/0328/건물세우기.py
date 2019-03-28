def dfs(n, nsum):
    global ans
    if n>=N:
        if nsum<ans: ans=nsum
        return
    if nsum>=ans: return
    for i in range(N):
        if chk[i]: continue
        chk[i] = 1
        dfs(n+1, nsum+arr[n][i])
        chk[i] = 0
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
chk = [0]*N
ans = 1000000
dfs(0,0)
print(ans)