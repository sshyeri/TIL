def M1(n):
    if n>=N:
        print(*result)
        return
    for i in range(1, 7):
        if result[n]: continue
        result[n] = i
        M1(n+1)
        result[n] = 0

def M2(n, k):
    if n>=N:
        print(*result)
        return
    for i in range(k, 7):
        if result[n]: continue
        result[n] = i
        M2(n+1, i)
        result[n] = 0

def M3(n):
    if n>=N:
        print(*result)
        return
    for i in range(6):
        if chk[i]: continue
        chk[i] = 1
        result[n] = i+1
        M3(n + 1)
        chk[i] = 0


N, M = map(int, input().split())
result = [0]*N
chk = [0]*6
if M==1: M1(0)
if M==2: M2(0, 1)
if M==3: M3(0)