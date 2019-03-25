import sys
sys.stdin = open("이진수_input.txt")
def HtoB(n):
    t = ''
    if n>'9': n = ord(n)-55
    else: n = int(n)
    for _ in range(4):
        t = str(n%2) + t
        n//=2
    return t


for tc in range(int(input())):
    N, num = input().split()
    ans = ''
    for n in num:
        ans += HtoB(n)
    print("#%d"%(tc+1), ans)