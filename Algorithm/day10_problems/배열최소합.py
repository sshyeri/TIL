import sys
sys.stdin=open("배열최소합_input.txt")

def permute(k, n, total):
    global mint
    if total >= mint:
        return
    if k==n:
        mint = min(mint, total)
        return
    else:
        for i in range(n):
            if not v[i]:
                v[i] = True
                permute(k+1, n, total + numbers[k][i])
                v[i] = False

for tc in range(int(input())):
    n = int(input())
    numbers=[list(map(int, input().split())) for i in range(n)]
    mint = 500
    for i in range(n):
        v = [False]*n
        v[i] = True
        permute(1, n, numbers[0][i])
    print(f'#{tc+1}',mint)