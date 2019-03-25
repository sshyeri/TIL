def babygin():
    global flag
    chk = 0

    if A[0] == A[1] == A[2] : chk += 1
    if A[4] == A[5] == A[5] : chk += 1

    if A[0]+2 == A[1]+1 == A[2] : chk +=1
    if A[3]+2 == A[4]+1 == A[5] : chk +=1

    if chk == 2:
        flag = 1
        print(A)
        return

def perm(n, k):
    if n==k: babygin()
    else:
        for i in range(k, n):
            A[i], A[k] = A[k], A[i]
            perm(n, k+1)
            A[i], A[k] = A[k], A[i]

A = list(map(int, input()))
flag = 0
perm(6, 0)

