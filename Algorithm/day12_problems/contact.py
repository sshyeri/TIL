import sys
sys.stdin = open("contact_input.txt")

for tc in range(1, 11):
    l, s = map(int, input().split())
    datas = list(map(int, input().split()))
    maps = {}
    Q = []
    chk = [0]*(max(datas)+1)
    for i in range(0,len(datas),2):
        if maps.get(datas[i]):
            maps[datas[i]] += [datas[i+1]]
        else:
            maps[datas[i]] = [datas[i+1]]

    Q.append(s)
    chk[s] = 1

    while Q:
        t = Q.pop(0)
        for i in maps.get(t,[]):
            if not chk[i]:
                Q.append(i)
                chk[i] = chk[t] + 1

    m = max(chk)
    for i in range(len(chk)-1,0,-1):
        if m == chk[i]: break

    print(f'#{tc}',i)