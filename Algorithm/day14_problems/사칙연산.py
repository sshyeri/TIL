import sys
sys.stdin = open("input.txt")
def calc(n1, op, n2):
    if op=="*":
        return n1*n2
    if op=="+":
        return n1+n2
    if op=="-":
        return n1-n2
    if op=="/":
        return n1//n2
def mktree(node):
    if data[node][3]:
        return data[node][3]
    else:
        data[node][3] = calc(mktree(data[node][1]), data[node][0], mktree(data[node][2]))
        return data[node][3]
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
            p = t[0]
        else:          
            data[t[0]][3] = int(t[1])
    mktree(1)
    # for i in range(p, 0, -1):
    #     data[i][3] = calc(data[data[i][1]][3], data[i][0], data[data[i][2]][3])
    print('#%d'%(tc+1), data[1][3])