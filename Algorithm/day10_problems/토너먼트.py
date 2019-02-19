import sys
sys.stdin = open('토너먼트_input.txt')

def div(i, j):
    if i == j:
        return i
    else:
        r1 = div(i, (i + j) // 2)
        r2 = div((i + j) // 2 + 1, j)
        if students[r1] == students[r2]:
            return r1
        elif students[r1] + students[r2] == 4:
            if students[r1] == 1:
                return r1
            else:
                return r2
        else:
            if students[r1] > students[r2]:
                return r1
            else:
                return r2

for tc in range(int(input())):
    n = int(input())
    students = list(map(int, input().split()))
    print(div(0, n - 1) + 1)
