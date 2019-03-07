def ABC(i, j):
    C = 0
    for k in range(i):
        C += score[k]
    if C > KMax or C < KMin: C = False
    B = 0
    for k in range(i, j):
        B += score[k]
    if B > KMax or B < KMin: B = False
    A=0
    for k in range(j, len(score)):
        A += score[k]
    if A > KMax or A < KMin: A = False
    if A and B and C: return max(A, B, C)-min(A, B, C)
    else: return False

for tc in range(int(input())):
    N, KMin, KMax = map(int, input().split())
    crew = list(map(int, input().split()))
    score = [0]*(max(crew)+1)

    for i in crew:
        score[i] += 1

    if max(score)>KMax: print(-1)
    else:
        ans = 1000
        for i in range(len(score)-1):
            for j in range(i+1, len(score)):
                if j<len(score)-1 and not score[j-1]+score[j]+score[j+1]:
                    continue
                else:
                    t = ABC(i, j)
                    if t: ans = min(ans, t)
        if ans==1000: print(-1)
        else: print(ans)
