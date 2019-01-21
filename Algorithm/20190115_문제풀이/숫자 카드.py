import sys
sys.stdin = open("sample_input_3.txt")

for tc in range(int(input())):
    cards = [0] * 10
    n = int(input())
    numbers = int(input())
    for i in range(n):
         cards[numbers%10] += 1
         numbers //= 10
    max_v = [0, 0]
    for i, c in enumerate(cards):
        if c >= max_v[1]:
            max_v[1] = c
            max_v[0] = i

    print(f"#{tc+1} {max_v[0]} {max_v[1]}")
