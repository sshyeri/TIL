def CountingSort(A, B, C):
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1


A = [1, 4, 5, 1, 2, 4, 5, 7, 9, 3]      #입력 배열
B = [0] * len(A)            #정렬된 배열
C = [0] * 10            #카운트 배열
CountingSort(A, B, C)
print(B)