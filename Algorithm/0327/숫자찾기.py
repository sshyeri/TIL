
def binSearch(s, e, data):
    while s<=e:
        m = (s+e)//2
        if data==arr[m]: return m+1
        elif data>arr[m]: s = m+1
        else: e = m-1
    return 0
N = int(input())
arr = list(map(int, input().split()))
T = int(input())
fff = list(map(int, input().split()))
# A = [0]*(arr[-1]+1)
# for i in range(N): A[arr[i]] = i+1
# for i in fff:
#     if i>arr[-1]: print(0)
#     else: print(A[i])
for i in fff:
    print(binSearch(0, N-1, i))
