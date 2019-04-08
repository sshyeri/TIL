for tc in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    Q = []
    dr = (1, -1, 0, 0)
    dc = (0, 0, 1, -1)
    for i in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                Q.append((i, j))
                arr[i][j] = 0
                cnt += 1
                while Q:
                    r, c = Q.pop(0)
                    for k in range(4):
                        nr, nc = r+dr[k], c+dc[k]
                        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc]:
                            arr[nr][nc] = 0
                            Q.append((nr, nc))
    print(cnt)