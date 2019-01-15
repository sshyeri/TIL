if __name__ == '__main__':
    scores = []
    names = []
    for _ in range(int(input())):
        names += [input()]
        scores += [float(input())]
    print(names)
    print(scores)
    min_k = scores.index(min(scores))
    names.pop(min_k)
    scores.pop(min_k)
    ans = []
    for i in range(len(scores)):
        if scores[i] == min(scores):
            ans += [names[i]]
    ans.sort()
    print(ans)


