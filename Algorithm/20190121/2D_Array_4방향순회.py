def iswall(x, y):
    if x < 0 or y < 0 or x >= 5 or y >= 5:
        return True

arr = [[1, 1, 1, 1, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 1, 1, 1, 1]]

result = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if not iswall(testX, testY):
                result += abs(arr[y][x] - arr[testY][testX])
print(result)