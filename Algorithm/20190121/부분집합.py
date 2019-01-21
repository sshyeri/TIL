# bit = [0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             print(bit)


# arr = [1, 2, 3]
# n = len(arr)
#
# for i in range(1 << n):
#     for j in range(n):
#         if i & (1 << j):
#             print(arr[j], end =",")
#     print()

arr = [-7, -3, -2, 5, 8]
cnt = 0
for i in range(1, 2**len(arr)):
    subset = [arr[j] for j in range(len(arr)) if i & (1 << j)]
    if sum(subset) == 0:
        print(f'{subset} : True')
        cnt += 1
print(cnt)