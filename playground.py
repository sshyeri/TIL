def getTotalX(a, b):
    bcd=[]
    for i in range(max(a), min(b)+1):
        if min(b)%i == 0:
            bcd += [i]
    bcd = set(bcd)
    temp = bcd.copy()
    for i in b:
        for j in bcd:
            if i%j != 0 and j in temp:
                temp -= {j}
    bcd = temp
    result = bcd.copy()
    for i in bcd:
        for j in a:
            if i%j != 0 and i in result:
                result -= {i}
    print(result)
    print(len(result))
getTotalX([3, 4],[24, 48])