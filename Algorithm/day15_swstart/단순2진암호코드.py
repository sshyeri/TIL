import sys
sys.stdin = open("암호코드_input.txt")

code = ['0001101', '0011001', '0010011', '0111101', '0100011',
        '0110001', '0101111', '0111011', '0110111', '0001011']
def verify():
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j]=='1':
                odd, nsum = 0, 0
                for k in range(0,50,7):
                    p = code.index(''.join(map(str, arr[i][j-k-6:j-k+1])))
                    if k==0 or not (k//7)%2: nsum += p
                    else : odd += p
                if (3*odd + nsum)%10: return 0
                else: return odd+nsum
for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print("#%d"%(tc+1), verify())