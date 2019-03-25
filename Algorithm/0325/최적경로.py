import sys
sys.stdin = open("input.txt")

# def dist():
    # global ans
    # sums = abs(xy[0]-xy[a[0][0]]) + abs(xy[1]-xy[a[0][1]])
    # for i in range(N-1):
    #     if ans <= sums: return
    #     sums += abs(xy[a[i][0]]-xy[a[i+1][0]]) + abs(xy[a[i][1]]-xy[a[i+1][1]])
    # sums += abs(xy[2] - xy[a[-1][0]]) + abs(xy[3] - xy[a[-1][1]])
    # if ans > sums :
    #     ans = sums

def perm(n, k, sums):
    global ans
    if n==k:
        if sums<ans:
            ans=sums
    if sums>ans: return
    else:
        for i in range(k, n, sums):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1, sums+)
            a[i], a[k] = a[k], a[i]

for tc in range(int(input())):
    N = int(input())
    xy = list(map(int, input().split()))
    a = [i for i in range(1, N+1)]
    d=[[0]*(N+2) for _ in range(N+2)]
    for i in range(N+1):
        for j in range(i+1, N+2):
            d[i][j] = abs(xy[i*2]-xy[j*2])+abs(xy[i*2+1]-xy[j+2+1])
    print(*d)
    ans = 10000000000
    sums = 0
    perm(N, 0, 0)
    print("#%d"%(tc+1),ans)
