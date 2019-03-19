
for tc in range(int(input())):
    B = input()
    T = input()
    Bn, Tn = 0, 0
    for i in B:
        Bn = 2*Bn + int(i)
    for i in T:
        Tn = 3 * Tn + int(i)
    print(Bn, Tn)