def catch(): 
    while Q:
        r, c = Q.pop(0)
        for i in range(8):
            newr, newc = r+dr[i], c+dc[i]
            if newr==S and newc==K: return arr[r][c]
            if 0<=newr<N and 0<=newc<M and not arr[newr][newc]:
                arr[newr][newc] = arr[r][c]+1
                Q.append((newr, newc))

N, M = map(int, input().split())
R, C, S, K = map(lambda x: int(x)-1, input().split())
arr = [[0]*M for _ in range(N)]
arr[R][C] = 1
Q = [(R, C)]
dr = (-2,-2,-1,1,2,2,1,-1)
dc = (-1,1,2,2,1,-1,-2,-2)
print(catch())
