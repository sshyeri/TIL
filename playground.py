if __name__ == '__main__':
    N = int(input())
    a = []
    for i in range(N):
        s=input()
        if s[0] == 'i':
            a.insert(int(s.split()[1]),int(s.split()[2]))
        elif s[1] == 'o':
            print(a)
        elif s[2] == 'm':
            a.remove(int(s.split()[1]))
        elif s[0] == 'a':
            a.append(int(s.split()[1]))
        elif s[0] == 's':
            a.sort()
        elif s[0] == 'p':
            a.pop()
        else:
            a.reverse()                