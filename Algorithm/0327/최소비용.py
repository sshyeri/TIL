N = int(input())
ni = list(map(int, input().split()))
ans = 0
for s in range(N-1):
    for j in range(s, s+2):
        for i in range(s+1, N):
            if ni[j] > ni[i]: ni[j], ni[i] = ni[i], ni[j]
    ni[s+1] = ni[s]+ni[s+1]
    ans += ni[s+1]
print(ans)
