import sys
sys.stdin = open("input.txt") #제출 시 주석처리

for t in range(10):
    h, v, d1, d2 = 0, 0, 0, 0
    tc = int(input())
    data = [list(map(int, input().split())) for j in range(100)]
    for x in range(100):
        h = max(h, sum(data[x])) #각 행의 합
        v = max(v, sum([data[t][x] for t in range(100)]))  #각 열의 합
        d1 += data[x][x]
        d2 += data[x][99-x]
    print(f'#{tc} {max(h, v, d1, d2)}')

