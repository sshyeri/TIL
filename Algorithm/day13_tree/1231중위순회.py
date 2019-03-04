import sys
sys.stdin = open("1231_input.txt")

def inorder(node):
    node = int(node)
    if node and tree[node-1]:
        inorder(tree[node-1][2])
        print(tree[node-1][1], end="")
        inorder(tree[node-1][3])

for tc in range(1, 11):
    tree = [input().split() for _ in range(int(input()))]
    for i in tree:
        while len(i) < 4:
            i.append(0)
    print("#%d"%(tc), end=" ")
    inorder(1)
    print()