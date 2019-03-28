
N = int(input())
fibo = [1, 1]+[0]*(N-2)
for i in range(2,N):
    if not fibo[i]: fibo[i] = fibo[i-1]+fibo[i-2]
print(fibo[N-1])