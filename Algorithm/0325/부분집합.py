cnt = 0
N = 3
A = [0 for _ in range(N)]
data = [1, 2, 3]

def printset(n):
    global cnt
    cnt += 1
    print("%d : "%cnt, end="")
    for i in range(n):
        if A[i]==1:
            print("%d"%data[i], end="")
    print()

def powerset(n, k):
    if n==k:
        printset(n)
    else:
        A[k] = 1
        powerset(n, k + 1)
        A[k] = 0
        powerset(n, k+1)
powerset(N, 0)