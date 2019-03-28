def sums(n):
    if n==1: return 1
    else: return n + sums(n-1)
print(sums(int(input())))
