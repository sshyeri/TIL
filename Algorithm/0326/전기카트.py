import sys
sys.stdin = open("전기카트_input.txt")
def perm(n, k, sumv):
    global ans
    if sumv>ans: return
    if n==k:
        sumv += arr[A[k]][0]
        if sumv < ans: ans=sumv
    else:
        for i in range(k+1, n+1):
            A[i], A[k+1] = A[k+1], A[i]
            perm(n, k+1, sumv+arr[A[k]][A[k+1]])
            A[i], A[k+1] = A[k+1], A[i]

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = [i for i in range(N)]
    ans = 0x7fffffff
    perm(N-1, 0, 0)
    print("#%d"%(tc+1), ans)
