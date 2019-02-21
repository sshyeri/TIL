import sys
sys.stdin=open('forth_input.txt')

for tc in range(int(input())):
    s = list(map(str,input().split()))
    stack = []
    print(f'#{tc+1}', end=' ')
    for i in s:
        if i.isnumeric():
            stack.append(i)
        elif i=='.':
            if len(stack) == 1:
                print(*stack)
            else:
                print('error')
                break
        else:
            if len(stack) > 1:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(int(a)+int(b))
                elif i == '-':
                    stack.append(int(a)-int(b))
                elif i == '*':
                    stack.append(int(a)*int(b))
                elif i == '/':
                    stack.append(int(a)//int(b))
            else:
                print('error')
                break