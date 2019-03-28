def dfs(n, sums):
    global ans
    if n >= N:
        if ans>sums: ans=sums
        return
    if sums>ans: return
    for i in range(N):
        dfs(n+1, sums+arr[n][i])
def dfs2(n, sums):
    global ans
    if n >= N:
        if ans>sums: ans=sums
        return
    if sums>ans: return
    for i in range(N):
        if chk[i]: continue
        chk[i] = 1
        dfs2(n+1, sums+arr[n][i])
        chk[i] = 0
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
chk = [0]*N
ans = 10000000000
dfs(0,0)
print(ans)
ans = 10000000000
dfs2(0,0)
print(ans)