def process_solution(a, k):
    for i in range(1, k + 1):
        if a[i]: print(data[i], end=" ")
    print()


def process_sum(a, k, total):


    if total != 10: return

    for i in range(1, k + 1):
        if a[i]: print(data[i], end=" ")
    print()



def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2


def backtrack(a, k, input, total):
    if total > 10: return

    global MAXCANDIDATES, cnt
    c = [0] * MAXCANDIDATES

    if k == input:
        # process_solution(a, k)
        process_sum(a, k, total)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            if a[k]:
                backtrack(a, k, input, total + data[k])
            else:
                backtrack(a, k, input, total)
    cnt += 1


MAXCANDIDATES = 100
NMAX = 100
cnt = 0
# data = [0, 1, 2, 3]
data = [i for i in range(11)]
a = [0] * NMAX
# backtrack(a, 0, 3)
backtrack(a, 0, 10, 0)
print(cnt)