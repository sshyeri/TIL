n = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    mins = A[i]
    cnt = 0
    for j in range(i+1, n):
        if mins<A[j]:
            cnt += 1