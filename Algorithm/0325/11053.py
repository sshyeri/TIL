n = int(input())
A = list(map(int, input().split()))

ans = 0
if n == 1: print(1)
else:
    for i in range(n-1):
        cnt = 1
        m = A[i]
        for j in range(i+1, n):
            if m < A[j]:
                cnt += 1
                m = A[j]
                if ans >= n-1-j+cnt: break
        if cnt > ans: ans = cnt
    print(ans)