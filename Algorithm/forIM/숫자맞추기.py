cards = [list(map(int, input().split())) for _ in range(int(input()))]
players=[0]*len(cards)
for i in range(3):
    T={}
    for j in range(len(cards)):
        t = cards[j][i]
        if not T.get(t, 0):
            T[t]=[True, j]
            players[j]+=t
        elif T[t][0]:
            players[T[t][1]]-=t
            T[t][0]= False
for i in players:
    print(i)

