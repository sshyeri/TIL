def binarysearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if key == a[middle]:
            return middle, a[middle]
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return '검색을 실패했습니다.'
key = 4
data = [2, 4, 7, 9, 11, 19, 23]
print(binarysearch(data, key))