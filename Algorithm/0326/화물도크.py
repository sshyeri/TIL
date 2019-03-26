import sys
sys.stdin = open("화물도크_input.txt")

for tc in range(int(input())):
    N = int(input())
    arr = [0]*25
    p = 25
    for i in range(N):
        s, e = map(int, input().split())
        if not arr[e] or arr[e] < s:
            arr[e] = s
            if e < p: p = e
    cnt = 1
    i = p
    while i < 25:
        if arr[i] and arr[i] >= p:
            cnt += 1
            p = i
        i+=1
    print("#%d"%(tc+1),cnt)


