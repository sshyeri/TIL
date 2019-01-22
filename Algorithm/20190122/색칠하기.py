import sys
sys.stdin=open("1_input.txt")
import pprint

for tc in range(1, int(input())+1):
    ground = [[0]*10 for i in range(10)]
    cnt = 0
    for n in range(int(input())):
        r1, c1, r2, c2, idx = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                ground[i][j] += idx
                if ground[i][j] == 3:
                    cnt += 1
    print(f'#{tc} {cnt}')