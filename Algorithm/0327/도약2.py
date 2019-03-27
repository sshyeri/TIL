def upperSearch2(s, e, data):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if lotus[m]<data:
            s = m+1
            sol = m
        else: e = m-1
    return sol
N = int(input())
lotus = []
for _ in range(N):
    lotus.append(int(input()))
lotus.sort()
cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        start = lotus[j]+(lotus[j]-lotus[i])
        end = lotus[j]+2*(lotus[j]-lotus[i])
        cnt += upperSearch2(j, N-1, end+1)-upperSearch2(j, N-1, start)
print(cnt)

