import sys
sys.stdin = open("암호코드스캔_input.txt")

nums = [[2, 1, 1], [2, 2, 1], [1, 2, 2], [4, 1, 1],
        [1, 3, 2], [2, 3, 1], [1, 1, 4], [3, 1, 2],
        [2, 1, 3], [1, 1, 2]]

def HtoB(n):
    t = ''
    for _ in range(4):
        t = str(n%2) + t
        n//=2
    return t

HEXS = [HtoB(n) for n in range(16)]

def mkcode(r,s,e):
    code = arr[r][s:e+1]
    for i in range(10):   code = code.replace(str(i), HEXS[i])
    for i in range(10, 16):  code = code.replace(chr(ord('A')+i-10), HEXS[i])
    return code

def check(i):
    global p, tag, ans, odd, T
    p += 1
    t = [0,0,0]
    while i>=0 and code[i]=='1':
        t[2] += 1 
        i -= 1
    while i>=0 and code[i]=='0':
        t[1] += 1 
        i -= 1
    while i>=0 and code[i]=='1':
        t[0] += 1 
        i -= 1    
    while p!=8 and i>=0 and code[i]=='0': i -= 1
    if p==1:  tag = min(t)
    if tag>1:
        for k in range(3):  t[k]//=tag    
    for num in range(10):
        if t == nums[num]:
            if p%2: ans += num
            else: odd += num
            return i+1
    return -1

for tc in range(int(input())):
    R, C = map(int, input().split())
    arr = [input() for _ in range(R)]
    ANS = 0
    for r in range(R): 
        c = C-1
        while c>0:
            if arr[r][c]!='0' and (r==0 or arr[r-1][c]=='0'): 
                t = c
                cnt0=0
                while t>=0 and (r==0 or arr[r-1][t] =='0'): 
                    t -= 1
                    if t and arr[r][t]=='0' and arr[r][t-1]=='0': cnt0+=1
                    if cnt0 >= 16: break
                code = mkcode(r, t+1, c) 
                i = len(code)   
                T, p, tag, ans, odd = 0, 0, 0, 0, 0
                while i>0:
                    i -= 1
                    if code[i]=='1':
                        T = True
                        i = check(i)
                        if p==8 and not (ans + odd*3)%10:
                            ANS += ans+odd
                            p, ans, tag, odd = 0, 0, 0, 0
                            T = False
                    elif T: break
                c = t
            c -= 1    
    print("#%d"%(tc+1), ANS)