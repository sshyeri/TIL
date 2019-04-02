import sys
sys.stdin = open("연산_input.txt")

d = (1, -1, -10)
def calc():
    Q = [N]
    idx = 0
    while True:
        num = Q[idx]
        for i in range(4):
            if i==3: t = num
            else: t = d[i]
            tnum = num + t
            if 0<tnum<=1000000:
                if not dp[tnum] or dp[tnum] > dp[num]+1:
                    Q.append(tnum)
                    dp[tnum] = dp[num]+1
            if tnum==M: return
        idx += 1
for tc in range(int(input())):
    N, M = map(int, input().split())
    dp = [0]*1000001
    calc()
    print("#%d"%(tc+1), dp[M])
