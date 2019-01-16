import sys
sys.stdin = open("sample_input_2.txt")

def countcharging(k, n, m, distance):
    cnt = 0
    bus = k     # 버스 현재 연료
    if n//k > m:
        return 0
    for i in distance:
        if i > k:
            return 0
    for i in range(len(distance)-1):
        bus -= distance[i]
        if distance[i+1] > bus:     #앞으로 갈 거리가 현재 연료보다 크면
            cnt += 1
            bus = k
    return cnt

for tc in range(1, int(input())+1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))
    distance = [charge[0]-0]    # 첫번째 충전소 - 출발지 거리
    for i in range(m-1):
        distance += [charge[i+1] - charge[i]]       # 충전소 간의 거리
    distance += [n-charge[-1]]              # 마지막 충전소 - 도착지 거리
    print(f"#{tc} {countcharging(k, n, m,distance)}")