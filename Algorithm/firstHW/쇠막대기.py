s = input()
t, c, i = 0, 0, 0
while i<len(s):
    if s[i:i+2]=='()':
        i += 2
        c += t
    elif s[i]=='(':
        t += 1
        i += 1
    elif s[i]==')':
        c += 1
        t -= 1
        i += 1
print(c)
    