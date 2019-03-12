N = int(input())
nums = list(map(int, input().split()))
safe = [[0]*(2*N-1) for _ in range(2*N-1)]

for i in range(N):
    j=N-1-i
    for k in range(i+1):
        safe[i][j]=nums.pop(0)
        j+=2
for i in range(N,2*N-1):
    j = i+1-N
    for k in range(N-j,0,-1):
        safe[i][j]=nums.pop(0)
        j+=2
pw = [0]*(2*N-1)
for i in range(2*N-1):
    for j in range(2*N-1):
        if safe[j][i]:
            pw[i] += safe[j][i]
print(max(pw))