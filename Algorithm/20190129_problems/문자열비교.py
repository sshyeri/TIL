import sys
sys.stdin = open('문자열비교_input.txt')

# 보이어 무어 알고리즘
def strfind(key, text):
    i, j = len(key)-1, len(key)-1
    while j < len(text):
        if i==-1:
            return 1
        if key[i] != text[j]:
            for k in range(i-1,-1,-1):
                if key[k] == text[j]: 
                    j += len(key)-k-1
                    break
            else: 
                j += len(key)
            i = len(key)-1
        else:
            i -= 1
            j -= 1
    else:
        return 0   

for tc in range(1, int(input())+1):
    print(f'#{tc} {strfind(input(), input())}')
