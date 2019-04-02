import sys
sys.stdin = open("보급로_input.txt")

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    D = [[987654321]*N for _ in range(N)]
    D[0][0] = 0
    Q = [(0, 0)]
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<N and 0<=nc<N:
                if D[nr][nc] > D[r][c]+arr[nr][nc]:
                    D[nr][nc] = D[r][c]+arr[nr][nc]
                    Q.append((nr, nc))
    print("#%d"%(tc+1),D[N-1][N-1])