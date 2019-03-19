n = int(input()) #실수

def Nbin(n):
    if n==1: return '1'
    if n==0: return '0'
    else:
        return Nbin(n//2) + str(n%2)
print(Nbin(n))