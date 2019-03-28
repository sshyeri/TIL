N = int(input())
K = int(input())

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

fruit = [list(map(int, input().split())) for _ in range(K)]
L = int(input())

for i in range(L):
    t, d = input().split()
    t = int(t)
