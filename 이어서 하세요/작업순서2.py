import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    v, e = map(int, input().split())
    s = list(map(int,input().split()))

    post = [s[i] for i in range(0,v,2)]
    aft = [s[i] for i in range(1,v,2)]

    result = []

    for i in aft:
        if i not in post:
            result = result + [i]
        else:
            result = [i] + result

    print(tc)
    print(post)
    print(aft)
    print()
    print(result)
    print()
