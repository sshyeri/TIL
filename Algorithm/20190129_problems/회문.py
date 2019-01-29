import sys
sys.stdin = open('회문_input.txt')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    data = [input() for i in range(n)]
    if n == m:
        for p in range(n):
            i, j = 0, m-1
            if data[p][i] == data[p][j]:
                while i < m//2:
                    i += 1
                    j -= 1
                    if data[p][i] != data[p][j]:
                        break
                else:
                    print(f'#{tc} {data[p]}')
            if data[i][p] == data[j][p]:
                while i < m//2:
                    i += 1
                    j -= 1
                    if data[i][p] != data[j][p]:
                        break
                else:
                    print(f'#{tc}', ''.join([data[i][p] for i in range(n)]))
    else:                   
        for p in range(n):
            for i in range(n-m+1):
                j = i + m - 1
                if data[p][i] == data[p][j]:
                    while i < j:
                        i += 1
                        j -= 1
                        if data[p][i] != data[p][j]:
                            break
                    else:
                        print(f'#{tc}', ''.join([data[p][k] for k in range(i-m//2, j+m//2+1)]))
                        break
            for i in range(n-m+1):
                j = i + m - 1
                if data[i][p] == data[j][p]:
                    while i < j:
                        i += 1
                        j -= 1
                        if data[i][p] != data[j][p]:
                            break
                    else:
                        print(f'#{tc}', ''.join([data[k][p] for k in range(i-m//2, j+m//2+1)]))
                        break
        
                