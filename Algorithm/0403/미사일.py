def runch(i):
    global cnt, fire, wid
    for p in range(N):
        if abs(ship[p][0]-ship[i][0]) + abs(ship[p][1]-ship[i][1]) <= wid:
            if energy[p] > 0:
                energy[p] -= fire
                if energy[p] <= 0:
                    chk[p] = 1
                    cnt -= 1
            else: energy[p] -= fire
    return cnt

def resave(i):
    global cnt, fire, wid
    for p in range(N):
        if abs(ship[p][0] - ship[i][0]) + abs(ship[p][1] - ship[i][1]) <= wid:
            energy[p] += fire
            if 0<energy[p] <= fire:
                chk[p] = 0
                cnt += 1

def perm(n, C):
    global ans, cnt
    if n>=K:
        if ans > C:
            ans = C
        return

    for i in range(n, N):
        if chk[i]: continue
        pick[n] = i
        perm(n+1, runch(i))
        resave(i)

N = int(input())
ship = [list(map(int, input().split())) for _ in range(N)]
energy = [ship[i][2] for i in range(N)]
K, fire, wid = map(int, input().split())
pick = [0]*K
chk = [0]*N
cnt = N
ans = N
perm(0, N)
print(ans)
# 3
# 100 100 40
# 100 200 80
# 300 500 40
# 2 40 100