import sys
sys.stdin = open('회문2_input.txt')

for _ in range(10):
    tc = '#'+input()
    data = [input() for i in range(100)]

    count = []
    for p in range(100):
        #odd
        for j in range(1, 99):
            # 가로
            i = j-1
            k = j+1
            if data[p][i] == data[p][k]:
                count.append(3)
                while (k < 99 and i > 0):
                    i -= 1
                    k += 1
                    if data[p][i] != data[p][k]:
                        break
                    else:
                        count[-1] += 2  
            #세로
            i = j-1
            k = j+1             
            if data[i][p] == data[k][p]:
                count.append(3)
                while (k < 99 and i > 0):
                    i -= 1
                    k += 1
                    if data[i][p] != data[k][p]:
                        break
                    else:
                        count[-1] += 2                
        #even
        for j in range(99):
            #가로
            i = j
            k = j+1
            if data[p][i] == data[p][k]:
                count.append(2)
                while (k < 99 and i > 0):
                    i -= 1
                    k += 1
                    if data[p][i] != data[p][k]:
                        break
                    else:
                        count[-1] += 2
            #세로
            i = j
            k = j+1
            if data[i][p] == data[k][p]:
                count.append(2)
                while (k < 99 and i > 0):
                    i -= 1
                    k += 1
                    if data[i][p] != data[k][p]:
                        break
                    else:
                        count[-1] += 2
    print(tc, max(count))                