# def leap(i):
#     for p in range(i, len(lotus)-1):
#
lotus = sorted([int(input()) for _ in range(int(input()))])
d = [lotus[i]-lotus[i-1] for i in range(1, len(lotus))]
result = []

e = 0
while e<len(lotus):

print(lotus)
print(d)
print(result)