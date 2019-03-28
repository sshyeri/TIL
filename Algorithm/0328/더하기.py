def dfs(n, nsum):
    global P
    if P or nsum>K: return
    if n>=N:
        if nsum==K:
            P = 1
        return
    dfs(n+1, nsum+arr[n])
    dfs(n+1, nsum)
for tc in range(int(input())):
    N, K = map(int, input().split())
    arr=list(map(int, input().split()))
    P = 0
    dfs(0,0)
    if P: print("YES")
    else: print("NO")