N = int(input())
area = [0]*1001
mH = (0,0)
mnL = 1000
mxL = 0
for _ in range(N):
    L, H = map(int, input().split())
    if H > mH[1]:
        mH = (L, H)
    if L > mxL:
        mxL = L
    if L < mnL:
        mnL = L
    area[L] = H
cnt = 0
h = area[mnL]
w = 0
for i in range(mnL, mH[0]+1):
    if area[i]>h:
        w += cnt*h
        h = area[i]
        cnt = 0
    if area[i]==mH[1]:
        w += (mH[0]-i)*mH[1]
        break
    cnt+=1    
cnt = 0
h = area[mxL]
for i in range(mxL, mH[0]-1, -1):
    if area[i]>h:
        w += cnt*h
        h = area[i]
        cnt = 0
    if area[i]==mH[1]:
        w += (mH[0]-i)*mH[1]
        break
    cnt+=1
w += mH[1]
print(w)
