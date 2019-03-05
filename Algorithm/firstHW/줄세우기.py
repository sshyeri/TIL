#12:27
n = int(input())
p = list(map(int, input().split()))
ans = [1]
for i in range(1,n):
    if not p[i]: ans.append(i+1)
    else: ans.insert(-(p[i]),i+1)
print(*ans)
#12:36