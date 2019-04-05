dr = (1, -1, 0, 0)
dc = (0, 0, -1, 1)

def search(i, j, p):
    global tag
    temp = []
    Q = [(i, j)]
    while Q:
        i, j = Q.pop(0)
        temp.append((i, j))
        for k in range(4):
            ni, nj = i + dr[k], j + dc[k]
            if 0<=ni<12 and 0<=nj<6 and arr[ni][nj]==p and not chk[ni][nj]:
                chk[ni][nj] = 1
                Q.append((ni, nj))
    if len(temp)>=4:
        for k in temp:
            arr[k[0]][k[1]] = '.'
            tag = 1


def down():
    global C
    for i in range(6):
        temp = []
        k = 0
        for j in range(11, 0, -1):
            if arr[j][i]=='.':
                if not k: k = j
                if arr[j-1][i] != '.':
                    temp.append(arr[j-1][i])
                    arr[j-1][i] = '.'
        while temp:
            arr[k][i] = temp.pop(0)
            k -= 1


for T in range(int(input())):
    arr = [list(input()) for _ in range(12)]
    cnt = 0
    # while True:
    tag, C = 0, 0
    while True:
        chk = [[0]*6 for _ in range(12)]
        for i in range(11, -1, -1):
            for j in range(6):
                if arr[i][j] != '.' and not chk[i][j]:
                    chk[i][j] = 1
                    search(i, j, arr[i][j])
        if tag:
            cnt += 1
            tag = 0
            down()
        else: break

    print(cnt)