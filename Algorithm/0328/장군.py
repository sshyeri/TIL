def catch():
    while Q:
        r, c = Q.pop(0)
        for i in range(8):
            tr, tc = r+dr[i][2], c+dc[i][2]
            if tr==R2 and tc==C2: return arr[r][c]
            if 0<=tr<10 and 0<=tc<9 and not arr[tr][tc] :
                for j in range(2): 
                    if arr[r+dr[i][j]][c+dc[i][j]] == -1: break
                else:             
                    arr[tr][tc] = arr[r][c] + 1                   
                    Q.append((tr, tc))
    return arr[R2][C2]
arr = [[0]*9 for _ in range(10)]
R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())
arr[R1][C1], arr[R2][C2] = 1, -1
dr = ((-1, -2, -3),(-1,-2,-3),(0,-1,-2),(0,1,2),(1,2,3),(1,2,3),(0,1,2),(0,-1,-2))
dc = ((0,-1,-2),(0,1,2),(1,2,3),(1,2,3),(0,1,2),(0,-1,-2),(-1,-2,-3),(-1,-2,-3))
Q = [(R1, C1)]
print(catch())

    