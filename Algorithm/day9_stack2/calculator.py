#1: 연산자를 만나면 push, 아니면 출력
def postfix_1(str):
    stack=[]
    result=''
    operators = '+-*/'
    for i in str:
        if i in operators:
            stack.append(i)
        else:
            result += i

    while stack:
        result += stack.pop()
    return result


#내가 만든 후위연산표기
def mypost(s):
    result =''
    stack=[0,]
    operators = {'+':1, '-':1, '*':2, '/':2}
    for i in s:
        if i.isnumeric():
            result += i
        elif i=='(':
            stack += i
        elif i==')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        elif operators.get(i,0) > operators.get(stack[-1],0):
            stack += i
        else:
            while operators.get(i,0) <= operators.get(stack[-1],0):
                result += stack.pop()
            stack += i
    stack.pop(0)
    while stack:
        result += stack.pop()
    return result

str="2+3*4/5"
str2='(6+5*(2-8)/2)'
print(postfix_1(str))
print(mypost(str2))

# s = input()
#
# print(hu(s))