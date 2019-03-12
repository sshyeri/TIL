def no():
    return l<3 or max(c)>KMax or (l==3 and min(c)<KMin)
def Acnt(T2):
    cnt = 0
    for k in range(T2, l):
        cnt += c[k]
    if cnt>KMax or cnt<KMin: return False
    return cnt
def Bcnt(T1, T2):
    cnt = 0
    for k in range(T1, T2):
        cnt += c[k]
    if cnt > KMax or cnt < KMin: return False
    return cnt

def Ccnt(T1):
    cnt = 0
    for k in range(T1):
        cnt += c[k]
    if cnt > KMax or cnt < KMin: return False
    return cnt

def result():
    ans = 1000
    for i in range(l - 1):
        for j in range(i + 1, l):
            A,B,C = Acnt(j), Bcnt(i, j), Ccnt(i)
            if A and B and C:
                print("T1:",s[i],"T2:",s[j], C, B, A)
                ans = min(ans, max(A,B,C)-min(A, B, C))
    return ans
for tc in range(int(input())):
    N, KMin, KMax = map(int, input().split())
    crew = list(map(int, input().split()))
    score = {}

    for i in crew:
        if score.get(i):
            score[i] += 1
        else:
            score[i] = 1

    s = list(score.keys())
    c = list(score.values())
    l = len(s)
    print(s)
    print(c)
    print(l)
    if no(): print(-1)
    else:
        ans = result()
        if not ans or ans==1000: ans=-1
        print(ans)
