N = list(map(int, input()))
arr = [0]*9
for i in N:
    if i==9: arr[6] += 1
    else: arr[i] += 1
arr[6]/=2
if arr[6]%1: arr[6] = arr[6]//1 + 1
print(int(max(arr)))