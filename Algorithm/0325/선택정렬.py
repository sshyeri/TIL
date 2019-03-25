def SelectionSort(A):
    n = len(A)
    for i in range(n-1):
        minn = i
        for j in range(i+1, n):
            if A[j] < A[minn]:
                minn = j
        temp = A[minn]
        A[minn] = A[i]
        A[i] = temp

def SelectionSort2(A, s, e):
    mini = s
    if s==e: return
    for j in range(s+1, e, 1):
        if A[j] < A[mini]:
            mini = j
    A[s], A[mini] = A[mini], A[s]
    SelectionSort2(A, s+1, e)

A = list(map(int, input()))

SelectionSort2(A, 0 , len(A))
print(A)