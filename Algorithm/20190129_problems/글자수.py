import sys
sys.stdin = open('글자수_input.txt')

for tc in range(int(input())):
    chk = {i:0 for i in input()}
    str2 = input()
    for i,c in chk.items():
        for j in str2:
            if i == j:
                chk[i] += 1
    max_c = 0
    for c in chk.values():
        if c > max_c:
            max_c = c
    print(f'#{tc+1} {max_c}')
