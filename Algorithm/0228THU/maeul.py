def search(i,j):
    global f
    for k in range(4):
        ni, nj = i+dy[k], j+dx[k]
        if not hill[ni][nj] >= hill[i][j]:
            return 0
    f = True
    return 1

def setp():
    for i in range(0, N):
        for j in range(0, N):
            if hill[i][j]:
                return 1
    return 0
N = int(input())
hill = [list(map(int, input())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

p=setp()
if p:
    f = True
    while f:
        f = False
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                if hill[i][j] == p :
                    hill[i][j] += search(i, j)
        if f: p+=1
print(p)
# def iswall(i, j):
#     global N
#     return i==0 or j==0 or i==N-1 or j==N-1
#
# def search(i, j):
#     minh = 10000
#     if iswall(i, j):
#         return 0
#     for p in range(4):
#         ni, nj = i+dy[p], j+dx[p]
#         if not hill[ni][nj]:
#             return 0
#         else:
#             if minh > hill[ni][nj]:
#                 return 1
#     return minh
#
# def maxh(mh, i, j):
#     if mh < hill[i][j]:
#         return hill[i][j]
#     else:
#         return mh
#
# N = int(input())
# hill = [list(map(int, input())) for _ in range(N)]
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# mh = 0
# for i in range(N):
#     for i in range(N):
#         if hill[i][j]:
#
# # t = N
# # p = 0
# # while t>0:
# #     i, j = p, p
# #     for k in range(t):
# #         if hill[i][j+k]:
# #             hill[i][j+k] += search(i, j+k)
# #             mh = maxh(mh, i, j+k)
# #         if hill[t-1][j+k]:
# #             hill[t-1][j + k] += search(t-1, j+k)
# #             mh = maxh(mh, t-1, j + k)
# #     i+=1
# #     for k in range(t-1):
# #         if hill[i+k][j]:
# #             hill[i+k][j] += search(i+k, j)
# #             mh = maxh(mh, i+k, j)
# #         if hill[i+k][t-1]:
# #             hill[i+k][t-1] += search(i+k, t-1)
# #             mh = maxh(mh, i+k, t-1)
# #     t-=1
# #     p+=1
#
# print(hill)
# print(mh)
