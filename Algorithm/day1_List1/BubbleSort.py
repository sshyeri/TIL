def BubblesSort(data):
    for i in range(len(data)-1, 0, -1): #4 3 2 1
        for j in range(0, i):   # 0 1 2 3 / 0 1 2 / 0 1 / 0
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                print(i, j, data)

data = [55, 7, 78, 12, 42]
BubbleSort(data)
data.sort()
data.reverse()
print(data)

