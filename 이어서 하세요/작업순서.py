import sys
sys.stdin = open("input.txt")

#위상정렬
def chk():
    for i in range(1,v+1):
        if degree[i] == 0:
            result.append(i)
            degree[i] -= 1
            for j in range(1, v+1):
                if i in post[j]:
                    degree[j] -= 1

for tc in range(1, 11):
    v, e = map(int, input().split())
    s = list(map(int,input().split()))
    post = [[] for i in range(v+1)]
    for i in range(0,len(s)-1,2):
        post[s[i+1]] += [s[i]]

    degree = [len(post[i]) for i in range(v+1)]
    result = []





    # for i in range(1, v+1):
    #     if not post[i] and not visited[i]:
    #         visited[i] = True
    #         result.append(i)
    #     elif post[i]:
    #         min_idx = len(result)
    #         for j in post[i]:
    #             if visited[j]:
    #                  p = result.index(j)
    #                  min_idx = min(min_idx, p)
    #             else:
    #                 result.append(j)
    #                 visited[j] = True
    #         result.insert(min_idx, i)
    #         visited[i] = True
    print(post)
    print(degree)
    print(result)
    # print(f'#{tc}', *result)
# def search(n):
#     if visited[n]:
#
#     result.append(n)
