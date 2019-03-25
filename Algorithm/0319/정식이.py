
def Tchange(Bt, Tn):
    Tex = len(Tn)
    for i in range(1, len(Tn)):
        Tex -= 1
        if B[i]=='0':
            Tt  = Tn + 3**Tex
            if Bt==Tt: return Tt
            Tt = Tn + 3 ** Tex
            if Bt == Tt: return Tt
        elif B[i]=='1':
            Tt = Tn + 3 ** Tex
            if Bt == Tt: return Tt
            Tt = Tn - 3 ** Tex
            if Bt == Tt: return Tt
        else:
            Tt = Tn - 3 ** Tex
            if Bt == Tt: return Tt
            Tt = Tn - 3 ** Tex
            if Bt == Tt: return Tt
    return False
for tc in range(int(input())):
    B = input()
    T = input()
    Bn, Tn = 0, 0
    for i in B:
        Bn = 2*Bn + int(i)
    for i in T:
        Tn = 3 * Tn + int(i)
    Bex = len(B)
    for i in range(1, len(B)):
        Bex -= 1
        if B[i]=='1':
            Bt = Bn-2**(Bex)
            Tchange(Bt, Tn)
        else:
            Bt = Bn+2**(Bex)

    print(Bn, Tn)