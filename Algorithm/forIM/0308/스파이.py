N, S = input().split()
N = int(N)
i, p = 0, 0
while p <len(S):
    if S[p]=='<': i += 1
    elif S[p]=='>': i -= 1
    elif i == N:
        while S[p].isdigit():
            print(S[p], end="")
            p += 1
        print(end=" ")
        p -= 1
    p += 1
