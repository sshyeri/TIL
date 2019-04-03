import sys
sys.stdin = open("input.txt")
def DFS(n, sour, bitter):
    global ans
    if n>=N:
        if bitter and ans > abs(sour-bitter): ans = abs(sour-bitter)
        return
    DFS(n+1, sour*s[n], bitter+b[n])
    DFS(n+1, sour, bitter)
N = int(input())
s = [0]*N
b = [0]*N
ans = 1000000000
for i in range(N):
    s[i], b[i] = map(int, input().split())
DFS(0, 1, 0)
print(ans)