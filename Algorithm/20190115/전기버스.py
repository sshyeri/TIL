import sys
sys.stdin = open("sample_input_2.txt")

def countcharging(knm, distance):
    cnt = 0
    bus = knm[0]
    if knm[1]//knm[0] > knm[2]:
        return 0
    for i in distance:
        if i > knm[0]:
            return 0
    for i in range(len(distance)-1):
        bus -= distance[i]
        if distance[i+1] > bus:
            cnt += 1
            bus = knm[0]
    return cnt


for tc in range(1, int(input())+1):
    knm = list(map(int, input().split()))
    charge = list(map(int, input().split()))
    distance = [charge[0]-0]
    for i in range(knm[2]-1):
        distance += [charge[i+1] - charge[i]]
    distance += [knm[1]-charge[-1]]
    print(f"#{tc} {countcharging(knm,distance)}")