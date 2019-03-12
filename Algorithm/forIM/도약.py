temp = [int(input()) for _ in range(int(input()))]

print(temp)

cnt = 0
for i in range(len(lotus)-2):
    for j in range(i+1, len(lotus)-1):
        d = lotus[j]-lotus[i]
        
        for k in range(j+1, len(lotus)):
            if d+lotus[j]<= lotus[k] <= 2*d+lotus[j]:
                cnt += 1
                print(lotus[i], lotus[j], lotus[k])
            if lotus[k]>2*d:
                break
print(cnt)        

