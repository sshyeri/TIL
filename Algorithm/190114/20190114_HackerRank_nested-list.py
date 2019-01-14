if __name__ == '__main__':
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores += [name, score]
    print(min(scores))


