import sys
sys.stdin = open('미로_input.txt')

def moseri(i,j):
    global n
    return not(i < 0 or j < 0 or i > n-1 or j > n-1)

def search(i,j):
    global chk

    for p in range(4):
        newi = i + dx[p]
        newj = j + dy[p]
        if moseri(newi, newj):
            if not miro[newi][newj]:
                miro[newi][newj] = 1
                search(newi, newj)
            if miro[newi][newj] == 3:
                chk = 1
                return
        
for tc in range(int(input())):
    n = int(input())
    miro = [list(map(int,list(input()))) for i in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    chk = 0
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                search(i,j)
                break
    print(f'#{tc+1}',chk)