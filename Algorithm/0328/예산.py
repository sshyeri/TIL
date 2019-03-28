def chk(m):
    tot = 0
    for i in range(N):
        if JB[i] <= m : tot += JB[i]
        else: tot += m
    if tot <= M : return 1
    else: return 0

N = int(input())
JB = list(map(int, input().split()))
M = int(input())

e = max(JB)
s = 1
sol = 0
while s <= e:
    m = (s+e)//2
    if chk(m):
        sol = m
        s = m+1
    else: e = m-1
print(sol)
