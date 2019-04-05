def findst():
    r = []
    b = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                r = [i, j]
            if arr[i][j] == 'B':
                b = [i, j]
            if r and b:
                chk[r[0]][r[1]][b[0]][b[1]]
                return tuple(r+b+[0])
def play():
    while Q:
        Rr, Rc, Br, Bc, cnt = Q.pop(0)
        if cnt>=10: return -1
        for i in range(4):
            nRr, nRc, nBr, nBc = Rr+dr[i], Rc+dc[i], Br+dr[i], Bc+dc[i]
            if arr[nRr][nRc]=='#':
                nRr, nRc = Rr, Rc
            if arr[nBr][nBc]=='#':
                nBr, nBc = Br, Bc
            if nRr == nBr and nRc == nBc: continue
            if arr[nBr][nBc]=='H': continue
            if arr[nRr][nRc]=='H' : return cnt+1
            if not chk[nRr][nRc][nBr][nBc]:
                chk[nRr][nRc][nBr][nBc] = 1
                Q.append((nRr, nRc, nBr, nBc, cnt+1))
    return -1
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
for T in range(int(input())):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    chk = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    Q = [findst()]
    print(play())