N = int(input())
ds = [[] for _ in range(5)]

# 긴거 전 후 맥스에서 민 빼기
for i in range(6):
    d, t = map(int, input().split())
    ds[d] += [[i, t]]

idx = []
s = 1
for i in ds:
    if len(i)==1:
        s*=i[0][1]
        if i[0][0] - 1 == -1: idx.append(5)
        else: idx.append(i[0][0] - 1)    
        idx.append((i[0][0]+1)%6)
ms = 1
for i in ds:
    if len(i)>1:
        for j in i:
            if j[0] not in idx:
                ms *= j[1]

print((s-ms)*N)