# N = int(input())
# R, C = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(R)]
# print(N)
# print(R, C)
# for i in arr:
#     for j in i:
#         print(j, end="")
#     print()

# 2진수 7비트 단위로 끊어서 10진수로 출력하기
# arr =  [0,0,0,0,0,0,0,1,1,1, 1,0,0,0,0,0,0,1,1,0, 0,0,0,0,0,1,1,1,1,0,
#         0,1,1,0,0,0,0,1,1,0, 0,0,0,1,1,1,1,0,0,1, 1,1,1,0,0,1,1,1,1,1, 1,0,0,1,1,0,0,1,1,1]
#
# for i in range(10):
#     n = 0
#     for j in range(i*7, i*7+7):
#         n = n*2 + arr[j]
#     print(n, end=" ")
# print()

def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

for i in range(-5, 6):
    print("%3d = " %i, end='')
    Bbit_print(i)

a = 0x86
key = 0xAA

print("a      ==> ", end='')
Bbit_print(a)

print("a^=key ==> ", end='')
a ^= key
Bbit_print(a)

print("a^=key ==> ", end='')
a ^= key
Bbit_print(a)