C, R = map(int, input().split())
K = int(input())

if K>C*R: print(0)
else:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    first = True
    ga = True
    x, y = 1, 1
    i, n = 0, 1

    for _ in range(K-1):
        x += dx[i]
        y += dy[i]
        n += 1
        if n==R and ga:
            i = (i+1)%4
            n=1
            ga = False
            if first: first = False
            else: R-=1
        if n==C and not ga:
            i = (i + 1) % 4
            n = 1
            ga = True
            C-=1

    print(x, y)
