import sys
sys.stdin=open("2_input.txt")

for tc in range(1, int(input())+1):
    a = [i for i in range(1, 13)]
    result = 0
    n, k = map(int, input().split())
    for i in range(1,1<<len(a)):
        subset = [a[j] for j in range(len(a)) if i & (1 << j)]
        if sum(subset) == k and len(subset)==n:
            result += 1
    print(f'#{tc} {result}')
