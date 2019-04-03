def DFS(n, Lbf, Lsum, Rbf, Rsum):
    global ans
    if n>=N:
        if Lsum + Rsum > ans: ans = Lsum + Rsum
        return
    if not Lbf or box[n] < Lbf:
        DFS(n + 1, box[n], Lsum + box[n], Rbf, Rsum)
    if not Rbf or box[n] > Rbf:
        DFS(n + 1, Lbf , Lsum , box[n], Rsum + box[n])
    DFS(n + 1, Lbf, Lsum, Rbf, Rsum)
for tc in range(int(input())):
    N = int(input())
    box = list(map(int, input().split()))
    ans = 0
    DFS(0,0,0,0,0)
    print(ans)