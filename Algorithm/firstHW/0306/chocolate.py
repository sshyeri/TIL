N = int(input())
cnt = 0
for _ in range(N):
    H, L = input().split()
    h, l = set(H), set(L)
    if len(h)<len(H) or len(l)<len(L) or len(h&l)>1:
        cnt += 1
print(cnt)