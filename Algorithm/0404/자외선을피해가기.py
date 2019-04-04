def djik():
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            tr, tc = r + dr[i], c + dc[i]
            if 0 <= tr < N and 0 <= tc < N and D[tr][tc] > D[r][c] + arr[tr][tc]:
                D[tr][tc] = D[r][c] + arr[tr][tc]
                Q.append((tr, tc))
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)
D = [[9999999]*N for _ in range(N)]
D[0][0] = 0
Q = [(0, 0)]
djik()
print(D[N-1][N-1])
