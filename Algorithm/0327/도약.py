def lowerSearch(s, e, data):
    sol = -1
    while s <= e:
        m = (s+e)//2
        if arr[m] >= data:
            sol = m
            e = m-1
        else: s = m+1
    return sol
def upperSearch(s, e, data):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if arr[m] <= data:
            sol = m
            s = m+1
        else: e = m-1
    return sol
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
cnt = 0
for i in range(N-2):
    for j in range(N-1):
        start = arr[j] + (arr[j]-arr[i])
        end = arr[j] + (arr[j]-arr[i])*2
        lo = lowerSearch(j+1, N-1, start)
        if lo==-1 or arr[lo]>end: continue
        up = upperSearch(j+1, N-1, end)
        cnt += (up-lo+1)
print(cnt)