def findst():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 3: 
                arr[i][j] = 0
                chk[3][i][j] = 1
                return(i, j, 3, 0)

def escape():
    while Q:
        r, c, bomb, cnt = Q.pop(0)
        if arr[r][c]==4:
            return cnt
        for i in range(4):
            tr, tc = r + dr[i], c + dc[i]
            if 0<=tr<R and 0<=tc<C:
                if arr[tr][tc]==1:
                    continue
                if arr[tr][tc]==4:
                    return cnt + 1
                if not arr[tr][tc] and not chk[bomb][tr][tc]:
                    chk[bomb][tr][tc] = 1
                    Q.append((tr, tc, bomb, cnt+1))
                if bomb and arr[tr][tc] == 2 and not chk[bomb-1][tr][tc]:
                    chk[bomb-1][tr][tc] = 1
                    Q.append((tr, tc, bomb-1, cnt+1))
    return -1

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)
R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
chk = [[[0]*C for _ in range(R)] for i in range(4)]
Q = [findst()]
print(escape())
