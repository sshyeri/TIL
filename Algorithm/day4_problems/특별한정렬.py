import sys
sys.stdin=open("4_input.txt")

for tc in range(1, int(input())+1):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(0, 10):
        max_a, min_a = i, i
        for j in range(i+1, len(a)):
            if a[min_a] > a[j]:
                min_a = j
            if a[max_a] < a[j]:
                max_a = j
        if i%2:
            a[i], a[min_a] = a[min_a], a[i]
        else:
            a[i], a[max_a] = a[max_a], a[i]
    
    print(f'#{tc}', end = ' ')
    for i in range(10):
        print(a[i], end = ' ')
    print()
