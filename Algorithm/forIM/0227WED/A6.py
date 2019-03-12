p = [list(map(int, input().split())) for _ in range(int(input()))]
w = [[0]*100 for _ in range(100)]

for a in p:
    for i in range(a[0], a[0]+10):
        for j in range(a[1], a[1]+10):
            w[i][j] = 1
cnt = 0
for a in w:
    cnt += a.count(1)
print(cnt)