def rotate90(square):
    temp = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N-1, -1, -1):
            temp[i].append(square[j][i])
    return temp

N = int(input())
square = [list(map(int, input().split())) for _ in range(N)]

while 1:
    n = int(input())
    if not n: break
    if n not in [90, 180, 270, 360]: continue
    if n==360:
        for i in square:
            print(*i)
        continue
    if n>=90:
        square = rotate90(square)[:]
    if n>=180:
        square = rotate90(square)[:]
    if n>=270:
        square = rotate90(square)[:]      
    for i in square:
        print(*i)
