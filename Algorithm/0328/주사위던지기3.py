def dfs(n, nsum):
    if n>=N:
        if nsum==M: print(*rec)
        return
    if nsum>M: return
    for i in range(1, 7):
        rec[n] = i
        dfs(n+1, nsum+i)

N, M = map(int, input().split())
# chk = [0]*7
rec = [0]*N
dfs(0, 0)