N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

ms = 1
plate = sushi[:k]
for p in range(N):
    plate.pop(0)
    plate += [sushi[(p+k)%N]]
    ms = max(ms, len(set(plate+[c])))
print(ms)