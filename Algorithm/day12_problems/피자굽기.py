import sys
sys.stdin = open("피자굽기_input.txt")

for tc in range(int(input())):
    n, m = map(int, input().split())
    pizzas = [[i, j] for i, j in enumerate(list(map(int, input().split())),1)]

    hwa = pizzas[:n]
    pizzas = pizzas[n:]

    while pizzas or hwa:
        cheese = hwa.pop(0)
        cheese[1] //= 2
        if cheese[1]:
            hwa.append(cheese)
        elif pizzas:
            hwa.append(pizzas.pop(0))

    print(f'#{tc+1}',cheese[0])