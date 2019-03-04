#0304 12:02AM

t = []
for _ in range(5):
    s, e = map(float, input().split())
    n = e-s-1
    if n>0:
        if n>4:
            t.append(4)
        else:
            t.append(n)
a = sum(t)
if a>=15:
    print(int(a*10000*0.95))
elif a<=5:
    print(int(a*10000*1.05))
else:
    print(int(sum(t)*10000))

#12:23