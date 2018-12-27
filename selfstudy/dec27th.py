n = input()
a = 0
t = 1
for i in range(1,len(n)+1):
    a += (int(n[-i], base = 16)*t)
    t *= 16
print(a)
    
