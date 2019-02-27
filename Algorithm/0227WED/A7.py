# def wall(i, j):
#     return i<=0 or i>=99 or j<=0 or j>=99

N = int(input())
w = [[0]*101 for i in range(101)]

for k in range(N):
    r, c = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            w[i][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

for i in range(100):
    for j in range(100):
        if w[i][j]:
            for d in range(4):
                ni, nj = i+dy[d], j+dx[d]
                if not w[ni][nj]:
                    cnt += 1
print(cnt)




