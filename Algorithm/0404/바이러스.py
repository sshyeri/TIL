# def findSet(x):
#     while p[x] != x:
#         x = p[x]
#     return x
#
# def link(x, y):
#     if rank[x] > rank[y]: p[y] = x
#     else:
#         p[x] = y
#         if rank[x] == rank[y]: rank[y] += 1
#
# N = int(input())
# M = int(input())
# p = list(range(N + 1))
# rank = [0]*(N+1)
#
# for i in range(M):
#     x, y = map(int, input().split())
#     link(findSet(x), findSet(y))
# print(p.count(p[1])-1)
def FF(no):
    global sol
    chk[no] = 1
    sol += 1
    for i in range(N+1):
        if arr[no][i] and not chk[i]: FF(i)

N = int(input())
M = int(input())
chk = [0]*(N+1)
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    s, e = map(int, input().split())
    arr[s][e] = arr[e][s] = 1

sol = -1
FF(1)
print(sol)