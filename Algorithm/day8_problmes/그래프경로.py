import sys
sys.stdin=open("그래프경로_input.txt")

def search(s, g):
    visited[s] = True

    for w in G[s]:
        if visited[g]:
            return True
        if not visited[w]:
            search(w, g)

for tc in range(int(input())):

    v, e = map(int, input().split())
    G=[[] for j in range(v+1)]

    for i in range(e):
        s, g = map(int,input().split())
        G[s].append(g)

    s, g = map(int,input().split())
    visited = [False for _ in range(v+1)]

    search(s, g)

    if visited[g]:
        print(f'#{tc+1} 1')
    else:
        print((f'#{tc+1} 0'))
