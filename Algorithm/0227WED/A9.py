M = int(input())
mo = [input() for _ in range(M)]
P = int(input())
pattern = [input() for _ in range(P)]

cnt = 0
for i in range(M-P):
    for j in range(M-P):
        t = True
        for p in range(P):
            for q in range(P):
                if not mo[i+p][j+q]==pattern[p][q]:
                    t = False
                    break
        if t:
            cnt += 1
print(cnt)

for i in range(M-P,3):
    for j in range(M-P,3):
        if pattern[0]==mo[j:j+3]:
            