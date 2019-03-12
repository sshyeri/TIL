def iswall(x, y):
    return x>N or y>N or x<1 or y<1

d=[[(0,1)],[(0,1),(1,0),(0,-1),(-1,0)], [(0,1),(-1,0),(0,-1),(0,1)]]


N = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
K = int(input())

for _ in range(K):
    r, c = map(int, input().split())
    arr[r][c] = 1

L = int(input())
sd = [input().split() for _ in range(L)]

ans = True
P, i, j = 0, 0, 0
r, c = 1, 1
snake = [(r,c)]
l = 0
sec = 0
T=0
arr[r][c] = -1

while ans:
    sec += 1
    nr = r+d[i][j][0]
    nc = c+d[i][j][1]
    if iswall(nr, nc):
        ans = False
        break
    r, c = nr, nc
    snake.append((r,c))
    if not arr[r][c]:
        arr[snake[l][0]][snake[l][1]] = 0
        l += 1
    elif arr[r][c]==-1:
        ans = False
        break
    arr[r][c] = -1

    if int(sd[T][0])==sec:
        if sd[T][1]=='D': P += 1
        else: P -= 1
        if not P:
             i, j = 0, 0
        elif P<0:
             i = 2
             j = -P%4
        else:
             i = 1
             j = P%4
        T+=1

print(sec)
# l = 0
# r, c, p, i, j, sec = 1, 1, 0, 0, 0, 0
# ans = True
# snake = [(r, c)]
# for _ in range(L):
#     X, C = input().split()
#
#     if ans:
#         X = int(X)-sec
#         while X:
#             X -= 1
#             sec += 1
#             r += d[i][j][0]
#             c += d[i][j][1]
#             if iswall(r, c):
#                 ans = False
#                 break
#             if (r, c) in snake[l:]:
#                 ans = False
#                 break
#             snake += [(r, c)]
#             if field[r][c]:
#                 field[r][c] = 0
#             elif not field[r][c]:
#                 l += 1
#
#         if C == "D": p += 1
#         elif C == "L": p -= 1
#
#         if p < 0:
#             i = 2
#             j = -p%4
#         elif p > 0:
#             i = 1
#             j = p%4
#         elif p == 0:
#             i, j = 0, 0
#
# while ans:
#     sec += 1
#     r += d[i][j][0]
#     c += d[i][j][1]
#     if iswall(r, c):
#         ans = False
#         break
#     if (r, c) in snake[l:]:
#         ans = False
#         break
#     snake += [(r, c)]
#     if field[r][c]:
#         field[r][c] = 0
#     elif not field[r][c]:
#         l += 1
#
# print(sec)
