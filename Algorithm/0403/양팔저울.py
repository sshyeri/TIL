def DFS(n, Lsum, Rsum):
    global sol
    if sol: return
    if Lsum==Rsum:
        sol = 1
        return
    if n>=CN: return
    DFS(n+1, Lsum+chu[n], Rsum)
    DFS(n+1, Lsum, Rsum+chu[n])
    DFS(n+1, Lsum, Rsum)
CN = int(input())
chu = list(map(int, input().split()))
BN = int(input())
ball = list(map(int, input().split()))
rec = [0]*CN
for i in range(BN):
    sol = 0
    DFS(0, ball[i], 0)
    if sol: print('Y', end=" ")
    else: print('N', end=" ")
