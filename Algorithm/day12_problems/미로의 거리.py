import sys
sys.stdin = open("미로의 거리_input.txt")
def out(i, j):
    return i<0 or j<0 or i>n-1 or j>n-1

def search():
    while Q:
        x, y = Q.pop(0)
        for p in range(4):
            nx, ny = x+dx[p], y+dy[p]
            if out(nx, ny): continue
            if miro[nx][ny] == '3':
                result.append((cnt[x][y])-1)
            if miro[nx][ny]=='0' and not cnt[nx][ny]:
                Q.append((nx, ny))
                cnt[nx][ny] = cnt[x][y] + 1

for tc in range(int(input())):
    n = int(input())
    miro = [input() for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = [[0]*n for _ in range(n)]
    Q = []
    result = []

    for i in range(n):
        for j in range(n):
            if miro[i][j] == '2':
                Q.append((i, j))
                cnt[i][j] = 1
                search()
                break
    if result:
        print(f'#{tc+1}', min(result))
    else:
        print(f'#{tc+1}', 0)