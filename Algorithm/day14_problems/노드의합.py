import sys
sys.stdin = open("노드의합_input.txt")

def postorder(node):
    if node>N: return 0
    if tree[node]:
        return tree[node]
    tree[node]= postorder(node*2)+postorder(node*2+1)
    return tree[node]

for tc in range(int(input())):
    N, M, L = map(int, input().split())
    tree=[0]*(N+1)
    for _ in range(M):
        i, n = map(int, input().split())
        tree[i] = n
    postorder(1)
    print("#%d"%(tc+1),tree[L])