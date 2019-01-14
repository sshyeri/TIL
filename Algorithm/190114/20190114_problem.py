import sys
sys.stdin = open("view_input.txt")  #제출 시 주석처리
T = 10
for tc in range(T):
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))
    for i in range(1, len(data)-2):
        if max(data[i-2],data[i-1],data[i],data[i+1],data[i+2]) == data[i]:
            ans += (data[i] - max(data[i-2],data[i-1],data[i+1],data[i+2]))

    print(f"#{tc+1} {ans}")
