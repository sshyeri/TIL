import sys
sys.stdin = open("input.txt")
def findmaxmin(boxes, idx):
    for i in range(len(boxes)):
        if boxes[idx[0]] < boxes[i]:
            idx[0] = i
        if boxes[idx[1]] > boxes[i]:
            idx[1] = i
    return idx
for tc in range(1, 11):
    limit = int(input())
    boxes = list(map(int, input().split()))
    idx = [0, 0]
    idx = findmaxmin(boxes, idx)
    boxes[idx[0]] -= 1  # 최대값
    boxes[idx[1]] += 1  # 최소값
    while limit > 1:
        idx = findmaxmin(boxes, idx)
        if boxes[idx[0]] - boxes[idx[1]] <= 1:
            break
        else:
            idx = findmaxmin(boxes, idx)
            boxes[idx[0]] -= 1  # 최대값
            boxes[idx[1]] += 1  # 최소값
        limit -= 1
    idx = findmaxmin(boxes, idx)

    print(f"#{tc} {boxes[idx[0]] - boxes[idx[1]]}")
