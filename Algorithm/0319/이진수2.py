import sys
sys.stdin = open("이진수2_input.txt")

for tc in range(int(input())):
    N = input()
    n = int(N[2:])
    p = 10**(len(N)-2)
    ans = ''
    while n:
        if len(ans)>12:
            ans = 'overflow'
            break
        n*=2
        ans += str(n//p)
        n%=p
    print("#%d"%(tc+1),ans)