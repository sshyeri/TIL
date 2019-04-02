import sys
sys.stdin = open("최소이동거리_input.txt")
for tc in range(int(input())):
    N, E = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        arr[s][e] = w
    for i in range(N+1):
        for j in range(i+1, N+1):
            if not arr[i][j]: arr[i][j] = 987654321
    for k in range(N+1):
        for i in range(N+1):
            if k==i: continue
            for j in range(i+1, N+1):
                if arr[i][k] and arr[k][j]: arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])
    print("#%d"%(tc+1), arr[0][N])