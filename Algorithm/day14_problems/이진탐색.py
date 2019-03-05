import sys
sys.stdin = open("이진탐색_input.txt")

def inorder(n):
    global i

    if n<=N:
        inorder(n*2)
        tree[n] = i
        i+=1
        inorder(n*2+1)

for tc in range(int(input())):
    N = int(input())

    tree=[0]*(N+1)
    i = 1
    inorder(1)
    print("#%d"%(tc+1), tree[1], tree[N//2])