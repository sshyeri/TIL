def Lcount(s, e, data):
    if e<0 or arr[e] != data : return e+1
    ls, le  = s, e
    while ls<=le:
        lm = (ls+le)//2
        if data > arr[lm]: ls = lm+1
        if data == arr[lm]: le = lm-1
    if arr[lm] != data: return le+1
    return lm

def Rcount(s, e, data):
    if s>N-1 or arr[s] != data: return s-1
    rs, re, = s, e
    while rs<=re:
        rm = (rs + re) // 2
        if data < arr[rm]: re = rm-1
        if data == arr[rm]: rs = rm+1
    if arr[rm] != data: return rs-1
    return rm

def binSearch(s, e, data):
    while s <= e:
        m = (s + e) // 2
        if data == arr[m]: return Rcount(m+1, N-1, data)-Lcount(0, m-1, data)+1
        elif data > arr[m]: s = m + 1
        else: e = m - 1
    return 0

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
farr = list(map(int, input().split()))

# parr = [0]*(arr[-1]+1)
# for i in arr: parr[i]+=1
# for i in farr:
#     if i>arr[-1]: print(0, end=" ")
#     else: print(parr[i], end=" ")

for i in farr:
    print(binSearch(0,N-1,i), end=" ")

