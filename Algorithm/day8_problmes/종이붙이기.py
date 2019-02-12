import sys
sys.stdin=open("종이붙이기_input.txt")

ans = [1, 3]
for tc in range(int(input())):
    n = int(input())
    for i in range(len(ans),n//10):
        ans.append(ans[i-1]+2*ans[i-2])
    print(f'#{tc+1} {ans[(n-1)//10]}')