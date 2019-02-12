def Bbit_print(a):
    for i in range(7, -1, -1):
        if a & (1<<i):
            print(1, end="")
        else:
            print(0, end="")
    print()

a = 0x86
key = 0xAA
print("a        ==> ")
Bbit_print(a)

print("a^=key ==> ")
a ^= key
Bbit_print(a)

print("a^=key ==> ")
a ^= key
Bbit_print(a)