import sys
sys.stdin = open("회전_input.txt")

for tc in range(int(input())):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    print(f'#{tc+1}', nums[m%len(nums)])