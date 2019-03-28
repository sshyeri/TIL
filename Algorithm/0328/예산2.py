N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr.sort()
sol, tot = 0, 0
for i in range(N):
    if tot + arr[i]*(N-i) <= M: tot += arr[i]
    else:
        sol = (M-tot)//(N-i)
        break
if not sol: print(arr[N-1])
else: print(sol)