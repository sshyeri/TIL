def preorder(node):
    if node:
        print(node, end=" ")
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node:
        inorder(tree[node][0])
        print(node, end=" ")
        inorder(tree[node][1])

def postorder(node):
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end=" ")


tree = [[0, 0, 0] for _ in range(int(input())+1)]
route = list(map(int, input().split()))


for i in range(0,len(route),2):
    tree[route[i+1]][2] = route[i]

for i in range(1, len(tree)):
    parent = tree[i][2]
    if parent:
        if tree[parent][0]:
            tree[parent][1] = i
        else:
            tree[parent][0] = i

for i in range(1, len(tree)):
    print("%3d %3d %3d %3d"%(i, *tree[i]))

preorder(1)
print()
inorder(1)
print()
postorder(1)
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

