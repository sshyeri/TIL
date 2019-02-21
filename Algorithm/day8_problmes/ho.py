import sys
sys.stdin = open("작업순서_input.txt")

T = 10

def DPS_route(S):
    global E, visited, test, V, stack
    
    for k in range(V + 1):
        if visited[k] == 0 and test[k][S] == 1:
            visited[k] = 1
            test[k][S] -= 1
            stack.append(k)
            if 100000 > max(test[k]) > 1:                   
                DPS_route(start())
            elif max(test[k])==0:
                DPS_route(k)
#시작점 찾기
def start():
    global test
    for S in range(1, len(test)):
        if max(test[S]) == 0:
            test[S][0]=100000
            visited[S] = 1
            stack.append(S)
            return S


for tc in range(T):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    test = [[0 for _ in range(V+1)] for _ in range(V+1)]
    x = []
    y = []
    visited = [0 for _ in range(V+1)]
    stack=[]


    #인접행렬
    for j in range(len(data)):
        if j % 2:
            x.append(data[j])
        else:
            y.append(data[j])


    for i in range(len(x)):
        test[x[i]][y[i]] = 1

    #스타트지점 S 찾기
    DPS_route(start())
    print("#{}".format(tc + 1), end=" ")
    for v in range(len(stack)):
        print(stack[v], end=" ")
    # print("#{} {}".format(tc + 1, stack))
    print()
