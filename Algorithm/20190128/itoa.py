def itoa(result,n):
    while (n > 0):
        result = [chr(ord('0') + n%10)] + result
        n//=10
    print(''.join(result))
n = int(input())
result = []
itoa(result,n)