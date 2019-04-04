def findst():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 3: return i, j
dr = (1, 0, 1, 0)
dc = (0, -1, 0, 1)
R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
r, c = findst()
bomb = 3
ans = 999999