def search(i, j):
    global P
    for p in range(P):
        for q in range(P):
            if not mo[i+p][j+q]==pattern[p][q]:
                return 0
    return 1
def search90(i, j):
    global P
    for p in range(P):
        for q in range(P):
            if not mo[i + p][j + q] == pattern[P-1-q][p]:
                return 0
    return 1
def search180(i, j):
    global P
    for p in range(P):
        for q in range(P):
            if not mo[i + p][j + q] == pattern[P-1-p][P-1-q]:
                return 0
    return 1
def search270(i, j):
    global P
    for p in range(P):
        for q in range(P):
            if not mo[i + p][j + q] == pattern[q][P-1-p]:
                return 0
    return 1
M = int(input())
mo = [input() for _ in range(M)]
P = int(input())
pattern = [input() for _ in range(P)]

cnt = 0
if not M or not P: print(cnt)
else:
    for i in range(M):
        for j in range(M):
            if i>M-P or j>M-P:
                break
            if pattern[0][0]==mo[i][j]:
                cnt += search(i, j)
            if pattern[P-1][0]==mo[i][j]:
                cnt += search90(i, j)
            if pattern[P-1][P-1]==mo[i][j]:
                cnt += search180(i, j)
            if pattern[0][P-1]==mo[i][j]:
                cnt += search270(i, j)
    print(cnt)

