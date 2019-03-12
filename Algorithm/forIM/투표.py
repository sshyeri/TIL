cand = [[0,0,0,0] for _ in range(4)]
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    cand[a][1] += 1
    cand[0][1] += a
    cand[b][2] += 1
    cand[0][2] += b
    cand[c][3] += 1
    cand[0][3] += c
score = max(cand[0])
ans = cand[0].index(score)
if cand[0].count(score)>1:
    if cand[3].count(max(cand[3]))>1:        
        if cand[2].count(max(cand[2]))>1:
            ans = 0
        else:
            ans = cand[2].index(max(cand[2]))
    else:
        ans = cand[3].index(max(cand[3]))
print(ans, score)
