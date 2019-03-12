def doughnut(i, j):
    t = 0
    t += sum(arr[i][j:j+K])
    t += sum(arr[i+K-1][j:j+K])
    for p in range(i+1, i+K-1):
        t += arr[p][j] + arr[p][j+K-1]
    return t

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

d = 0
for i in range(N-K+1):
    for j in range(N-K+1):
        d = max(d, doughnut(i, j))
print(d)
