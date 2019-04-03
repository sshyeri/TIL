def comb(n, r, s1, s2):
    global ans
    if r>=N//2:
        if abs(s1-s2) < ans:
            ans = abs(s1-s2)
        return
    if n>=N: return
    chk[n] = 1
    comb(n+1, r+1, s1-tapes[n], s2+tapes[n])
    chk[n] = 0
    comb(n+1, r, s1, s2)

N = int(input())
tapes = list(map(int, input().split()))
chk = [0]*N
SUM = sum(tapes)
ans = 500
comb(0, 0, SUM, 0)
print(ans)