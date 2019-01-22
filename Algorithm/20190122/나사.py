import sys
sys.stdin = open('nasa_input.txt')

for tc in range(1, int(input())+1):
    n = int(input())
    nasa = list(map(int, input().split()))

    for i in range(len(nasa)):
        cnt = 0
        for j in range(len(nasa)):
            if nasa[i] == nasa[j]:
                cnt += 1
                if cnt == 2:
                    break
        else:
            if i%2==0:
                result = [nasa.pop(i), nasa.pop(i)]                            
                break
    while len(result) < 2*n:
        for i in range(len(nasa)):
            if result[-1] == nasa[i]:
                if i%2:
                    result += [nasa.pop(i), nasa.pop(i-1)]                                       
                else:
                    result += [nasa.pop(i), nasa.pop(i)]                                      
                break

    print(f'#{tc}', *result)





