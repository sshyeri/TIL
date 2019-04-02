import sys
sys.stdin = open("그룹나누기_input.txt")

def findp(k):
    if p[k] == k: return k
    return findp(p[k])
def link(x, y):
    if rank[x] > rank[y]: p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]: rank[y] += 1
for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = list(range(N+1))
    rank = [0 for _ in range(N+1)]
    for i in range(M):
        p1 = findp(arr[i*2])
        p2 = findp(arr[i*2+1])
        link(p1, p2)
    cnt = 0
    for i in range(N+1):
        if i and i==p[i]: cnt += 1
    print("#%d"%(tc+1),cnt)