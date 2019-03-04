def preorder(node):
    global cnt
    if node:
        cnt+=1
        preorder(tree[node][0])
        preorder(tree[node][1])
def searchP(n1, n2):
    p1 = []
    t = tree[n1][2]
    while t:
        p1.append(t)
        t = tree[t][2]
    t = tree[n2][2]
    while t:
        if t in p1: return t
        t = tree[t][2]

for tc in range(1, int(input())+1):
    v, e, n1, n2 = map(int, input().split())
    route = list(map(int, input().split()))
    tree = [[0,0,0] for _ in range(v+1)]
    cnt = 0

    for i in range(0, len(route), 2):
        tree[route[i+1]][2] = route[i]
    for i in range(1, v+1):
        p = tree[i][2]
        if p:
            if tree[p][0]:
                tree[p][1] = i
            else:
                tree[p][0] = i
    cp = searchP(n1, n2)
    preorder(cp)
    print('#%d'%(tc),cp, cnt)