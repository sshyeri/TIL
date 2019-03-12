#12:40
def plus(s, x):
    for i in range(1, len(s)):
        sa = int(s[:i])
        sb = int(s[i:])
        if sa+sb==x:
            return str(sa)+'+'+str(sb)+'='+str(x)
    return 'NONE'
s, x = input().split()
print(plus(s, int(x)))
#12:45