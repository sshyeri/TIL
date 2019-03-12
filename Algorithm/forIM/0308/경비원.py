W, H = map(int, input().split())
N = int(input())
#한 줄로 놓고 계산
stores = [list(map(int, input().split())) for _ in range(N+1)]
result = []
for i in stores:
    if i[0]==1:
        result.append([i[1], 2*W+2*H-i[1]])
    elif i[0]==2:
        result.append(2*W+H-i[1])
    elif i[0]==3:
        result.append(2*W+2*H-i[1])
    else:
        result.append(W+i[1])
