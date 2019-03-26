import sys
sys.stdin = open("최대상금_input.txt")
def possible():
    l = len(num)
    t = 0
    if c*2 > l: return l
    if c*2 == l : return True
    for i in range(l):
        if num[i] != maxn[i]:
            t+=1
    if t == c*2: return True
    return False
for tc in range(int(input())):
    num, c = input().split()
    num = list(map(str, num))
    c = int(c)
    maxn = sorted(num, reverse=True)
    l = possible()
    if l is True or (l and (len(set(num)) < l or not (c-l//2)%2)) : print("#%d"%(tc+1),''.join(maxn))
    elif l:
        maxn[-1], maxn[-2] = maxn[-2], maxn[-1]
        print("#%d" % (tc + 1), ''.join(maxn))
    else:
        ct = 0
        while ct<c:
            mi = -1
            for i in range(len(num)-1,ct-1,-1):
                if num[mi] < num[i]: mi = i
            num[ct], num[mi] = num[mi], num[ct]
            ct += 1
        print("#%d" % (tc + 1), ''.join(num))

