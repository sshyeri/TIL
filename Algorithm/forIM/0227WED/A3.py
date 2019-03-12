# n = int(input())
# feed = {'N':[], 'Y':[]}
# for i in range(n):
#     a, b = input().split()
#     feed[b] += [int(a)]
#
# if not len(feed['Y']):
#     ans = 'F'
# else:
#     ans = min(feed['Y'])
#     if ans < max(feed['N']):
#         ans = 'F'
#
# print(ans)

# --------------------------------------

p = int(input())
n, y = 1, 10
for i in range(p):
    a, b = input().split()
    if b=='Y':
        y = min(y, int(a))
    else:
        n = max(n, int(a))
if y==10 or y<=n: print('F')
else : print(y)
