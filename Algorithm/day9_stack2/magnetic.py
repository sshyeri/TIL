import sys
sys.stdin = open("magnetic_input.txt")

for tc in range(1, 11):
    n = int(input())
    t = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    for i in range(n):
        p = False
        for j in range(n):
            if not p and t[j][i]==1:
                p = True
            elif p and t[j][i]==2:
                cnt += 1
                p = False

    print (f'#{tc}', cnt)
