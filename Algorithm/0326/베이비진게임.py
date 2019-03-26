import sys
sys.stdin = open("베이비진게임_input.txt")

def chkrun(arr):
    for i in range(1,9):
        if arr[i] and arr[i-1] and arr[i+1]: return True
    return False

for tc in range(int(input())):
    cards = list(map(int, input().split()))
    playerA = [0]*10
    playerB = [0]*10
    for i in range(0,12,2):
        playerA[cards[i]] += 1
        playerB[cards[i+1]] += 1
        if i >= 4:
            if 3 in playerA or chkrun(playerA):
                print("#%d"%(tc+1), 1)
                break
            elif 3 in playerB or chkrun(playerB):
                print("#%d" % (tc + 1), 2)
                break
    else:
        print("#%d" % (tc + 1), 0)