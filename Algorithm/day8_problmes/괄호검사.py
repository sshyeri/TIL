import sys
sys.stdin=open("괄호검사_input.txt")
f = ['(','{']
b = [')','}']

for tc in range(int(input())):
    chk = []
    for i in input():
        if i in f:
            chk.append(i)
        elif i in b:
            if not chk or (chk.pop() != f[b.index(i)]):
                print(f"#{tc+1} 0")
                break
    else:
        if chk:
            print(f"#{tc+1} 0")
        else:
            print(f"#{tc+1} 1")
