def chk(i, c):
    for k, p in enumerate(arr[i]):
        if p and color[k]==c: return False
    return True
def paint(i):
    global tag
    if i==N+1:
        tag = 1
        return
    for c in range(1, M+1):
        if chk(i, c):
            color[i] = c
            return paint(i+1)
    else: tag = 0
    return

N, M = map(int, input().split())
arr = [0] + [[0]+list(map(int, input().split())) for _ in range(N)]
color = [0]*(N+1)
tag = 1
paint(1)
color.pop(0)
if tag: print(*color)
else: print(-1)