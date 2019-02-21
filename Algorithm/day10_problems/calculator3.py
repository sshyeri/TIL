import sys
sys.stdin=open("calculator3_input.txt")

def mypost(s):
    result =''
    post=[0,]
    operators = {'+':1, '-':1, '*':2, '/':2}
    for i in s:
        if i.isnumeric():
            result += i
        elif i=='(':
            post += i
        elif i==')':
            while post[-1] != '(':
                result += post.pop()
            post.pop()
        elif operators.get(i,0) > operators.get(post[-1],0):
            post += i
        else:
            while operators.get(i,0) <= operators.get(post[-1],0):
                result += post.pop()
            post += i
    post.pop(0)
    while post:
        result += post.pop()
    return result
def cal(s):
    stack = []
    for i in s:
        if i.isnumeric():
            stack.append(i)
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
    return stack[0]
for tc in range(1, 11):
    n = int(input())
    print(f'#{tc}',cal(mypost(input())))
    