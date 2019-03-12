r1, c1, w1, h1 = map(int, input().split())
r2, c2, w2, h2 = map(int, input().split())

w = [[0]*20 for _ in range(20)]

for i in range(r1-1, r1+w1+1):
    for j in range(c1-1, c1+h1+1):
        if i==r1-1 or i==r1+w1 or j==c1-1 or j==c1+h1: w[i][j] = 2
        else: w[i][j] = 1

# for i in range(r1, r1+w1):
#     for j in range(c1, c1+h1):
#         w[i][j] = 1
# for i in range(r1-1, r1+w1+1):
#      w[i][c1-1] = 2
#      w[i][c1+h1] = 2
# for i in range(c1-1, c1+h1+1):
#     w[r1-1][i] = 2
#     w[r1+w1][i] = 2

cnt1 = 0
cnt2 = 0
for i in range(r2, r2+w2):
    for j in range(c2, c2+h2):
        if w[i][j]==1:
            cnt1 += 1
        elif w[i][j]==2:
            cnt2 += 1
if cnt1:
    print(3)
elif cnt2==1:
    print(1)
elif not cnt1 and not cnt2:
    print(4)
else:
    print(2)

