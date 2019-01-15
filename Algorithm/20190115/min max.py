import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    n =int(input())
    data = list(map(int, input().split()))
    min_v = data.pop(0)
    max_v = min_v
    for i in data:
        if max_v < i:
            max_v = i
        if min_v > i:
            min_v = i

    print(f"#{tc} {max_v-min_v}")