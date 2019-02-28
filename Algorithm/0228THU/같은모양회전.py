def search(i, j):
    global P
    for p in range(P):
        for q in range(P):
            if not mo[i+p][j+q]==pattern[p][q]:
                return 0
    return 1

M = int(input())
mo = [input() for _ in range(M)]
P = int(input())
pattern = [input() for _ in range(P)]

cnt = 0
if not M or not P: print(cnt)
else:
    for i in range(M):
        for j in range(M):
            if i>M-P or j>M-P:
                break
            if pattern[0][0]==mo[i][j]:
                cnt += search1(i, j)
    print(cnt)



# def search1(i, j, pattern1):
#     global P
#     for p in range(P):
#         for q in range(P):
#             if not mo[i+p][j+q]==pattern1[p][q]:
#                 return 0
#     return 1
# def search2(i, j, pattern2):
#     global P
#     for p in range(P):
#         for q in range(P):
#             if not mo[i+p][j+q]==pattern2[p][q]:
#                 return 0
#     return 1
# def search3(i, j, pattern3):
#     global P
#     for p in range(P):
#         for q in range(P):
#             if not mo[i+p][j+q]==pattern3[p][q]:
#                 return 0
#     return 1
# def search4(i, j, pattern4):
#     global P
#     for p in range(P):
#         for q in range(P):
#             if not mo[i+p][j+q]==pattern4[p][q]:
#                 return 0
#     return 1
#
# M = int(input())
# mo = [input() for _ in range(M)]
# P = int(input())
# pattern1 = [input() for _ in range(P)]
# pattern2 = [[] for _ in range(P)]
# pattern3 = [[] for _ in range(P)]
# pattern4 = [[] for _ in range(P)]
#
# for i in range(P):
#
#         pattern4[P-i-1] += pattern1[j][i]
# for i in pattern1:
#     print(i)
# for i in pattern2:
#     print(i)
# for i in pattern3:
#     print(i)
# for i in pattern4:
#     print(i)
#
# cnt = 0
# if not M or not P: print(cnt)
# else:
#     for i in range(M):
#         for j in range(M):
#             if i>M-P or j>M-P:
#                 break
#             if pattern1[0][0]==mo[i][j]:
#                 cnt += search1(i, j, pattern1)
#             if pattern2[0][0]==mo[i][j]:
#                 cnt += search2(i, j, pattern2)
#             if pattern3[0][0]==mo[i][j]:
#                 cnt += search3(i, j, pattern3)
#             if pattern4[0][0]==mo[i][j]:
#                 cnt += search4(i, j, pattern4)
#     print(cnt)