import sys
sys.stdin = open("반복문자지우기_input.txt")

def rmv(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return rmv(s[:i]+s[i+2:])
    return s

for tc in range(int(input())):
    s = input()
    print(f'#{tc+1} {len(rmv(s))}')