## LOTTO 당첨번호 Scraping

~~~python
from bs4 import BeautifulSoup
import requests
import random

numbers = random.sample(range(800, 838), 8) #로또 두달치 뽑기
for i in numbers:
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={i}"
    req = requests.get(url).text
    soup = BeautifulSoup(req,'html.parser') 
    print(f"{i} 회차 당첨번호")
    for j in soup.select(" .win .ball_645"):
        print(j.text, end=" ") #줄바꿈 안하고 띄어쓰기로
    print("+", soup.select_one(" .bonus .ball_645").text,"\n")


~~~

****



## 로또는 몇번만에 당첨될까?

*크롬 익스텐션 - json!*

      1. **random 으로 로또번호를 생성 (내가 사는 번호)**
      2. **api를 통해 우승번호를 가져오기**
      3. **0번과 1번을 비교해 나의 등수를 알려줌**

---

      1. **url 요청 보내서 정보를 가져옵니다.**
      - **json으로 받는다.(딕셔너리로 접근 가능)**
      2. **api의 당첨번호와 보너스 번호를 저장하고**
      3. **뽑은게 몇등인지 하는거 뽑으세요.**



### set

- 중복 허용x
- index없어요
- 출력은 중괄호지만 딕셔너리 아니에요
- 선언할때는 괄호로 선언해야해요



### 집합 연산

```bash
>>> set1 = set([1,2,3,4,5,6,7])
>>> set2 = set([5,6,7,8,9,10,11])
>>> set1.intersection(set2)
{5, 6, 7}
>>> set1 & set2
{5, 6, 7}
>>> set1.union(set2)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
>>> set1 | set2
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
>>> set1 - set2
{1, 2, 3, 4}
>>> set2 - set1
{8, 9, 10, 11}
```



### code

~~~python
import random
import requests
import json
from pprint import pprint

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()
win_num = []
for i in range(1,7):
    win_num.append(lotto[f"drwtNo{i}"])
win_num = set(win_num)
cnt = 0
while True:
    numbers = set(random.sample(range(1, 46), 6))
    # print(numbers)
    cnt += 1
    luck = len(numbers - win_num)
    if luck == 0:
        print(f"축하합니다! 1등입니다. 추첨 횟수 : {cnt}")
        break
    elif luck == 1:
        if lotto["bnusNo"] in numbers:
            print(f"축하합니다! 2등입니다. 추첨 횟수 : {cnt}")
            break
        else:
            print(f"축하합니다! 3등입니다. 추첨 횟수 : {cnt}")
            # break
    elif luck == 2 :
        print(f"축하합니다! 4등입니다. 추첨 횟수 : {cnt}")
        # break
    elif luck == 3 :
        print(f"축하합니다! 5등입니다. 추첨 횟수 : {cnt}")
~~~

[영화진흥위원회 API](http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)

https://api.telegram.org/bot758280023:AAEgZ1uYLV4C-8GNsf5kPcsUQUO2BvSLmQ0/getUpdates