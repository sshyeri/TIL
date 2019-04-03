#t: 소의 키들을 세워봤을 때, (1마리조합, 2마리 조합...N마리 조합)
def comb(n, hsum):
    global ans
    if n>=N:
        if 0 <= hsum-B < ans:
            ans = hsum-B
        return
    chk[n] = 1
    comb(n+1, hsum+H[n])
    chk[n] = 0
    comb(n+1, hsum)

for T in range(int(input())):
    N, B = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    chk = [0]*N
    ans = 1000000
    comb(0, 0)
    print(ans)