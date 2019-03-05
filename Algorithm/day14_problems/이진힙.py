import sys
sys.stdin = open("이진힙_input.txt")

def ancestors(n):
    global anc
    anc += tree[n]
    if n>1:
        ancestors(n//2)

def place(idx):
    if idx//2 and tree[idx//2]>tree[idx]:
        tree[idx//2], tree[idx] = tree[idx], tree[idx//2]
        place(idx//2)

for tc in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    anc = 0
    tree = [0]
    idx = 0

    for n in nums:
        tree.append(n)
        idx += 1
        place(idx)

    ancestors(idx//2)
    print("#%d"%(tc+1),anc)
