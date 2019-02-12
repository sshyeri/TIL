import sys
sys.stdin = open("3_input.txt")
def binarysearch(l, r, a, cnt):
    if (l + r)//2 == a:
        return cnt + 1
    elif (l + r)//2 < a:
        cnt += 1
        return binarysearch((l + r)//2, r, a, cnt)
    else:
        cnt += 1
        return binarysearch(l, (l + r)//2, a, cnt)
for tc in range(1, int(input())+1):
    p, a, b = map(int, input().split())
    rea = binarysearch(1, p, a, 0) 
    reb = binarysearch(1, p, b, 0)
    if rea == reb:
        print(f'#{tc} 0')
    elif rea > reb:
        print(f'#{tc} B')
    else:
        print(f'#{tc} A')