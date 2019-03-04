def chkga():
    cnt = 0
    for i in bingo:
        if not sum(i):
            cnt += 1
    return cnt
def chkse():
    cnt = 0   
    for i in range(5):
        sums = 0
        for j in range(5):
            sums += bingo[j][i]
        if not sums:
            cnt += 1
    return cnt
def chkdae():
    cnt = 0
    sums1 = 0
    sums2 = 0
    for i in range(5):
        sums1 += bingo[i][i]
        sums2 += bingo[i][5-1-i]
    if not sums1:
        cnt += 1
    if not sums2:
        cnt += 1
    return cnt
def erase(n):
    for p in range(5):
        for q in range(5):
            if bingo[p][q]==n:
                bingo[p][q]=0
                return
def play():
    c, C = 0, 0
    for i in call:
        for n in i:
            erase(n)
            c += 1
            if c>=12:
                C+=chkga()+chkse()+chkdae()
                if C>=3:
                    return c
                else:
                    C=0
bingo = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

print(play())
