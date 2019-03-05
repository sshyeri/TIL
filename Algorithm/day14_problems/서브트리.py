import sys
sys.stdin = open("서브트리_input.txt")

def search(node):
    global cnt
    if node:
        cnt += 1
        search(tree[node][0])
        search(tree[node][1])

for tc in range(int(input())):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    tree = [[0,0] for _ in range(E+2)]

    for i in range(0, 2*E, 2):
        if tree[nodes[i]][0]:
            tree[nodes[i]][1] = nodes[i+1]
        else:
            tree[nodes[i]][0] = nodes[i+1]

    cnt = 0
    search(N)
    print("#%d"%(tc+1), cnt)