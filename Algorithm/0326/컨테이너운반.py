import sys
sys.stdin = open("컨테이너운반_input.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort()
    truck.sort()
    ans = 0
    for i in range(M):
        if container:
            c = container.pop()
            while c > truck[-1]:
                if not container:
                    c = 0
                    break
                c = container.pop()
            ans += c
            truck.pop()
    print("#%d"%(tc+1),ans)