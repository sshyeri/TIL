C, R = map(int, input().split())
arr = [[0]*(C+1) for _ in range(R+1)]

N = int(input())
for i in range(N):
    d, x = map(int, input().split())

    if d==1:
        arr[0][x] = 1
    elif d==2:
        arr[R][x] = 1
    elif d==3:
       arr[x][0] = 1
    else:
        arr[x][C] = 1

d, x = map(int, input().split())
if d==1:
    arr[0][x] = 2
elif d==2:
    arr[R][x] = 2
elif d==3:
    arr[x][0] = 2
else:
    arr[x][C] = 2

for i in arr:
    print(i)