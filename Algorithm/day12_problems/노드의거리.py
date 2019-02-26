import sys
sys.stdin = open("노드의거리_input.txt")
def search():
    while Q:
        t = Q.pop(0)
        for i in range(v+1):
            if nodes[t][i] and not cnt[i]:
                Q.append(i)
                cnt[i] = cnt[t]+1
                if i==g: return
    cnt[g] = 1
    return

for tc in range(int(input())):
    v, e = map(int, input().split())
    route = [list(map(int, input().split())) for _ in range(e)]
    nodes = [[0]*(v+1) for _ in range(v+1)]
    s, g = map(int, input().split())
    cnt = [0]*(v+1)
    Q = []

    for i in route:
        nodes[i[0]][i[1]] = 1
        nodes[i[1]][i[0]] = 1

    Q.append(s)
    cnt[s] = 1
    search()

    print(f'#{tc+1}',cnt[g]-1)
