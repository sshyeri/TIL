import sys
sys.stdin = open("sample_input_4.txt")

for tc in range(1, int(input())+1):
    nm = list(map(int, input().split()))
    n = nm[0]
    m = nm[1]
    data = list(map(int, input().split()))
    result = [0] * (n-m+1)
    for i in range(m):
        result[0] += data[i]
    max_v = result[0]
    min_v = max_v
    for i in range(1, n-m+1):
        result[i] = result[i-1] - data[i-1]
        result[i] += data[i+m-1]
        if result[i] > max_v:
            max_v = result[i]
        if result[i] < min_v:
            min_v = result[i]
    print(f"#{tc} {max_v-min_v}")
