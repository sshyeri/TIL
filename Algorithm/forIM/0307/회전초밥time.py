N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

plate = {c:1}
for i in sushi[:k]:
    if plate.get(i):
        plate[i] += 1
    else:
        plate[i]=1

ms = len(plate.keys())
msb = ms

for p in range(N):
    bt = sushi[p]
    plate[bt] -= 1
    if bt!=c and not plate[bt]: msb -= 1
    at = sushi[(p+k)%N]
    if plate.get(at):
        plate[at] += 1
    else:
        plate[at] = 1
        msb += 1
    ms = max(ms, msb)
print(ms)