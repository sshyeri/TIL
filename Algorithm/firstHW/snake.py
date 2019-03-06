def iswall(x, y):
    return x>N or y>N or x<0 or y<0 

dD=[(0,1),(-1,0),(0,-1),(1,0)]
dL=[(0,1),(1,0),(0,-1),(-1,0)]

N = int(input())
field = [[0]*(N+1) for _ in range(N+1)]
K = int(input())

for _ in range(K):
    r, c = map(int, input().split())
    field[r][c] = 1
L = int(input())

S=[]
l = 1
r, c = 0, 0
sec = 0
ans = True
for _ in range(L):
    X, C = input().split()
    if ans:
        X = int(X)
        while X:
            sec+=1
            r+=dD[0][0]
            c+=dD[0][1]
            if iswall(r, c):
                ans=False
                break 
            elif field[r][c]: 
                l+=1
                field[r][c]=0
       #방향을 스택에 쌓아서 쌓인 방향만큼 dD, dL조정 

        