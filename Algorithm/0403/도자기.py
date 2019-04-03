def pick(n, r, p):
    global cnt
    if r>=M:
        cnt += 1
        return
    if n>=N: return
    for i in range(p, 26):
        if not kind[i]: continue
        kind[i] -= 1
        pick(n+1, r+1, i)
        kind[i] += 1

for tc in range(int(input())):
    N, M = map(int, input().split())
    sand = list(map(int, input().split()))
    kind = [0]*26
    for i in sand:
        kind[i-1] += 1
    cnt = 0
    pick(0, 0, 0)
    print(cnt)