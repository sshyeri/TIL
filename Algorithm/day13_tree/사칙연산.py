def calc(n1, node, n2):
    if node=="*":
        return n1*n2
    if node=="+":
        return n1+n2
    if node=="-":
        return n1-n2
    if node=="/":
        return n1/n2

def inorder(node):
    if node:
        if node.isdecimal():
            return node
        else:
            return(calc(inorder(tree[node][0], node, tree[node][1])))

for tc in range(1, 11):
    sik = [input().split() for _ in range(int(input()))]
    tree = [[0, 0, 0] for _ in range(len(sik)+1)]
    for i in sik:
        i[0]