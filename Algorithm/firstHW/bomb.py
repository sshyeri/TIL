def bomb(k, s):
    for i in p:
        s += int(i[0])
        if s>=210: return k
        if i[1]=='T':
            k = (k+1)%8
    return 7

k = int(input())-1
s = 0
p = [input().split() for _ in range(int(input()))]
print(bomb(k, s)+1)
    