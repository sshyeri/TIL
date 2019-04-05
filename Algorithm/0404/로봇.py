#python 3d list 는 [면][행][열]
def bfs():
    while Q:
        r, c, d, cnt = Q.pop(0)
        if r == s2 and c == e2 and d == d2: return cnt
        #L, R
        for i in range(2):
            td = turn[d][i]
            if r==s2 and c==e2 and td==d2: return cnt+1
            if not chk[td][r][c]:
                chk[td][r][c] = 1
                Q.append((r, c, td, cnt+1))
        #go1, 2, 3
        tr, tc = r+dr[d], c+dc[d]
        for i in range(3):
            if tr == s2 and tc == e2 and d == d2: return cnt+1
            if 0<=tr<N and 0<=tc<M:
                if not arr[tr][tc] and not chk[d][tr][tc]:
                    chk[d][tr][tc] = 1
                    Q.append((tr, tc, d, cnt+1))
                elif arr[tr][tc]: break
                tr += dr[d]
                tc += dc[d]
            else: break
    return -1
dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)
turn = ((3, 2), (2, 3), (0, 1), (1, 0))
N, M = map(int, input().split())
chk = [[[0]*M for _ in range(N)] for j in range(4)]
arr = [list(map(int, input().split())) for _ in range(N)]
s1, e1, d1 = map(lambda x: int(x) - 1, input().split())
s2, e2, d2 = map(lambda x: int(x) - 1, input().split())

Q = [[s1, e1, d1, 0]]
print(bfs())