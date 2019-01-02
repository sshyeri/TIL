#3. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, -2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}
#허용 method : max, min
coldest = ("서울", min(cities["서울"]))
hottest = ("서울", max(cities["서울"]))

for name, temp in cities.items() :   
    if min(temp) < coldest[1] : 
        coldest = (name, min(temp))
    if max(temp) > hottest[1] :
        hottest = (name, max(temp))
        
print(f"가장 추운 곳은 {coldest[0]} : {coldest[1]}도 입니다.")
print(f"가장 더운 곳은 {hottest[0]} : {hottest[1]}도 입니다.")
#print(f"가장 추운 곳은 {coldest} : {cold}도 입니다.\n가장 더운 곳은 {hottest} : {hot}도 입니다.")