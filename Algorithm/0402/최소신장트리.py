import sys
sys.stdin = open("최소신장트리_input.txt")

#prim
def findmin():
    global ans
    for i in range(V+1):
        if not mst[i][0]:
            minv = i
            break
    for i in range(V+1):
        if not mst[i][0] and mst[minv][1] > mst[i][1]:
            minv = i
    mst[minv][0] = 1
    ans += mst[minv][1]
    return minv

for tc in range(int(input())):
    V, E = map(int, input().split())
    data = [[] for _ in range(V+1)]
    for i in range(E):
        s, g, c = map(int, input().split())
        data[s].append((g, c))
        data[g].append((s, c))
    mst = [[0, 987654321, -1] for i in range(V+1)]
    mst[0][1] = 0
    ans = 0
    for _ in range(V+1):
        u = findmin()
        for v in data[u]:
            if not mst[v[0]][0] and v[1] < mst[v[0]][1]:
                mst[v[0]][2] = u
                mst[v[0]][1] = v[1]

    print("#%d"%(tc+1),ans)


