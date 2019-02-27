# def digitroot(n):
#     if n<10:
#         return n
#     else:
#         return digitroot(digitroot(n//10)+n%10)
# nums = sorted([int(input()) for _ in range(int(input()))])
# results = []
# for i in nums:
#     results.append(digitroot(i))
# print(nums[results.index(max(results))])
def digitroot(n):
    if n<10:
        return n
    else:
        return digitroot(digitroot(n//10)+n%10)

nums = [int(input()) for _ in range(int(input()))]
mxn, p = 0, 1000000
for i in nums:
    t = digitroot(i)
    if mxn == t and p > i:
        mxn, p = t, i
    elif mxn < t:
        mxn, p = t, i
print(p)

#선생님 풀이
def root_calc(num):
    while True:
        temp = list(map(int, str(num)))
        tot=sum(temp)
        if tot<10 : return tot
        num = tot

root_max = 0
sol = 0
for i in range(N):
    root = root_calc(arr[i])
    if root_max < root :
        root_max = root
        sol = arr[i]
    if root_max == root:
        sol = arr[i]
print(sol)