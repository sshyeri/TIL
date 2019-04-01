import sys
sys.stdin = open("test.txt")
def Dijkstra(s):
    U = [s]
    l = 1
    D = [0]*N
    for v in range(N):
        D[i] = arr[s][v]
    while l<N:
        U.append(D.index(min(D[i])))

for tc in range(int(input())):
    temp = list(map(int, input().split()))
    N = temp.pop(0)
    arr = [temp[i:i+N] for i in range(0, N*N, N)]
    for i in arr:
        if sum(i) == N-1:
            print("#%d"%(tc+1), N-1)
            break
    else:
        for i in range(N):
            for j in range(N):
                if i!=j and not arr[i][j]: arr[i][j] = 987654321



