def sort(s, e):
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
def Qsort(s, e):
    if s>=e: return
    p, t = e, s
    for l in range(s, e):
        if arr[l] < arr[p] and l!=t:
            arr[l], arr[t] = arr[t], arr[l]
            t+=1
    arr[p], arr[t] = arr[t], arr[p]
    Qsort(s, t-1)
    Qsort(t+1, e)

def Msort(s, e):
    if s>=e: return
    m = (s+e)//2
    Msort(s, m)
    Msort(m+1, s)
    l, r, t = s, m+1, s
    while l<=m and r<=e:
        if arr[l] < arr[r]:
            temp[t] = arr[l]
            t+=1; l+=1
        else:
            temp[t] = arr[r]
            t+=1; r+=1
    while l<=m:
        temp[t] = arr[l]
        t+=1; l+=1
    while r<=e:
        temp[t] = arr[r]
        t+=1; r+=1
    for i in range(s, e+1): arr[i] = temp[i]

#main-----------------------------------------------
N = int(input())
arr = list(map(int, input().split()))
temp=[0]*N

