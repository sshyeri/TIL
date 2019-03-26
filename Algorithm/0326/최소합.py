import sys
sys.stdin = open("최소합_input.txt")

def iswall(i, j):
    return i<0 or j<0 or i>N-1 or j>N-1

def search(i, j, sums):
    global ans
    if i == j == N-1:
        if ans > sums:
            ans = sums
            return
    if ans <= sums: return
    else:
        for k in range(2):
            newi, newj = i + dr[k], j + dc[k]
            if not iswall(newi, newj):
                search(newi, newj, sums+arr[newi][newj])

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [1, 0]
    dc = [0, 1]
    ans = 0x7fffffff
    search(0, 0, arr[0][0])
    print("#%d"%(tc+1),ans)

