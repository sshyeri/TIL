n = int(input())
c = 0
j = 1
for i in range(n-1, 0, -1):
    while n**2 >= i**2+j**2:
        c+=i
        j+=1

print(c*4)
