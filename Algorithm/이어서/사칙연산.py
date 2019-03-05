import sys
sys.stdin = open("input.txt")
def calc(n1, node, n2):
    if node=="*":
        return n1*n2
    if node=="+":
        return n1+n2
    if node=="-":
        return n1-n2
    if node=="/":
        return n1/n2

for tc in range(10):
    N = int(input())
    data = [[0]*4 for _ in range(N+1)]

    for _ in range(N):
        t = input().split()
        t[0] = int(t[0])
        if len(t)>2:
            data[t[0]][0] = t[1]
            data[t[0]][1] = int(t[2])
            data[t[0]][2] = int(t[3])
        else:
            data[t[0]][3] = int(t[1])

    print(data)