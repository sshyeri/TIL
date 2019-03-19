N = input()
b = ''
def change(p):
    t = ''
    for k in range(4):
        t = str(p % 2) + t
        p //= 2
    return t

for i in N:
    if i.isdecimal():
        b+=change(int(i))
    else:
        b += change(ord(i)-55)
print(b)

#7bit 단위 끊어서 10진수
for i in range(0,len(b),7):
    d = 0
    k = i
    while k<i+7 and k<len(b):
        d = d*2 + int(b[k])
        k += 1
    print(d, end=" ")
print()

#선생님
b = ''
asc = [change(i) for i in range(16)]

for i in N:
    if i<='9':
        b += asc[int(i)]
    else:
        b += asc[ord(i)-55]
print(b)