import sys
sys.stdin = open("GNS_test_input.txt", "r")

order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for c in range(int(input())):
    tc, dummy = map(str, input().split())
    numbers={}
    for i in map(str, input().split()):
        numbers[i] = numbers[i]+1 if i in numbers.keys() else 1
    print(tc)
    for i in order:
        print(f'{i} '*numbers[i], end = '')
