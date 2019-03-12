#90도 회전한 패턴
Parr90 = [[0]*P for _ in range(P)]
for i in range(P)
    for j in range(P):
        Parr90[j][P-i-1] = Parr[i][j]

#비교하기
for i in range(M-P+1):
    for j in range(M-P+1):
        cnt = 0
        for k in range(P)
            for i in range(P)