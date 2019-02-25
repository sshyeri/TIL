n, k = 7, 8
route = list(map(int, '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'.split()))
# 1 2 3 4 5 7 6

nodes = [[0]*(n+1) for _ in range(n+1)]
for i in range(k*2-1):
    nodes[route[i]][route[i+1]] = 1
    nodes[route[i+1]][route[i]] = 1

for i in nodes:
    print(i)

visited = [0] * (n+1)
Q = []
result = []
Q.append(route[0])
visited[Q[0]] = 1

while Q:
    t = Q.pop(0)
    result.append(t)

    for i in range(n+1):
        if nodes[t][i] == 1 and not visited[i]:
            Q.append(i)
            visited[i] = visited[t] + 1

print(*result)
print(*visited)
print(visited[result[-1]]-1)


