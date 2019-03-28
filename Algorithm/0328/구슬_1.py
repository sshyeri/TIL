a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
N = 3

def DFS(no): # a[no]번째 구슬을 상자에 담거나 담지 않는 모든 경우
# 1] 리턴조건 : N번째이면 인쇄후 리턴
    if no>=N:
        print(*b)
        return
    b[no] = a[no]
    DFS(no+1)
    b[no] = 0
    DFS(no+1)

#=================
DFS(0) # a[0]요소 구슬부터 시작