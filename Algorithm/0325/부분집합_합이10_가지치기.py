cnt = 0
N = 10
A = [0 for _ in range(N)]
data = [i+1 for i in range(10)]
sums = 0
total = 0
def sumset(n, sums):
    if sums == 10:
        printset(n)

def printset(n):
    global cnt
    cnt += 1
    print("%d : "%cnt, end="")
    for i in range(n):
        if A[i]==1:
            print("%d"%data[i], end="")
    print()

def powerset(n, k, sums):
    global total
    total += 1
    if sums > 10: return
    if n==k: sumset(n, sums)
    else:
        A[k] = 1
        powerset(n, k + 1, sums + data[k])
        A[k] = 0
        powerset(n, k+1, sums)

powerset(N, 0, 0)
print(total)