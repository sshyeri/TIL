n = int(input())
dotori = list(map(int, input().split()))
td = list(filter(lambda a:a>0, dotori))
if len(td):
    maxtd = sum(td)
else:
    maxtd = max(dotori)
md = [dotori[0]]
maxmd = md[0]
for i in range(1, n):
    md.append(max(dotori[i], dotori[i]+md[-1]))
    if maxmd<md[-1]:
        maxmd = md[-1]
print(maxmd, maxtd)


