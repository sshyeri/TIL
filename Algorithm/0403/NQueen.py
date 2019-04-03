dr = (-1, -1, -1)
dc = (-1, 0, 1)
def check(r, c):
    for i in range(3):
        for k in range(1, N):
            nr = r + k*dr[i]
            nc = c + k*dc[i]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc]: return 0
    return 1
def DFS(no):
    global sol
    if no>=N:
        sol += 1
        return
    # for i in range(N):
    #     if chk1[i]: continue
    #     if chk2[no+i]: continue
    #     if chk3[(N-1)-(no-i)]: continue
    #     chk1[i] = chk2[no+i] = chk3[(N-1)-(no-i)]=1
    #     DFS(no+1)
    #     chk1[i] = chk2[no+i] = chk3[(N-1)-(no-i)]=0


    for i in range(N):
        if check(no, i):
            arr[no][i] = 1
            DFS(no+1)
            arr[no][i] = 0
N = int(input())
arr = [[0]*N for _ in range(N)]
chk1 = [0]*N
chk2 = [0]*N*2
chk3 = [0]*N*2
sol = 0
DFS(0)
print(sol)
