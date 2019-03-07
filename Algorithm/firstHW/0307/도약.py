# N = int(input())
# lotus = sorted([int(input()) for _ in range(N)])
#
# cnt = 0
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             if lotus[j]-lotus[i] <= lotus[k]-lotus[j] <= 2*(lotus[j]-lotus[i]):
#                 cnt += 1
#             elif lotus[k]-lotus[j] > 2*(lotus[j]-lotus[i]):
#                 break
# print(cnt)
# def spot(p, minp, maxp):
#     global j, cnt
#     i = 1
#     while p+i<=N-1 or p-i>j:
#         if p-i>j and minp>lotus[p-i]: return
#         elif p+i<=N-1 and maxp<lotus[p+i]: return
#         else:
#             cnt+=1
#             i+=1
#     return


# 이진탐색
def binsearch(start, end, p):
    global cnt
    if start > end: return
    mid = (end+start)//2
    while start<=mid:
        if lotus[mid]>p:
            end = mid-1
        elif lotus[mid]<p:
           start = mid+1
        else:
            break
        mid = (end + start) // 2
    return mid

N = int(input())
lotus = sorted([int(input()) for _ in range(N)])

cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        x = lotus[j]-lotus[i]
        minp = lotus[j]+x
        maxp = lotus[j]+2*x
        if minp>lotus[-1]: break
        s = binsearch(j + 1, N - 1, minp)
        e = binsearch(j+1, N-1, maxp)
        if lotus[s]<minp: s+=1
        if lotus[e]>maxp: e-=1
        cnt += e-s+1
print(cnt)