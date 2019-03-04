a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
chk = [False, False] + [True]*b
cnt = 0
T = True
mins = 0
maxs = 0
for i in range(2, b+1):
    if chk[i]:
        if i>=a:
            cnt+=1
            if T:
                mins = i
                T = False
            else:
                maxs=i
        for j in range(2*i, b+1, i):
            chk[j]=False
print(cnt)
print(mins+maxs)