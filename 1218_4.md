## import requests

*pip install requests : 터미널에서 requests외장함수 설치*

1. requests.get(주소)
2. requests.get(주소).text
3. requests.get(주소).status_code



**정보 스크랩 1단계**

1. 원하는 정보가 있는 주소로 요청을 보내, 응답을 저장한다.

   1. import requests
   2. req=requests.get('주소').text

2. 정보를 출력하여 확인한다.

   1. print(req)



#### ***주소를 받고 응답받은 것을 예쁘게 만들어주고 원하는 것을 뽑아온다.***



**[beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) : 응답 코드를 예쁘게 만들어줌**

   > *pip install bs4 : 터미널에서 bs4외장함수 설치*

ex) soup = BeautifulSoup(req, 'html.parser')

~~~python
import requests #as req
#from bs4 import BeautifulSoup as bus
from bs4 import BeautifulSoup
req = requests.get("https://finance.naver.com/sise/").text 
#요청 받아서 텍스트화 시켜서 변수에 받아요
soup = BeautifulSoup(req, 'html.parser')    #받은걸 예쁘게 정리해서 수프에 넣어요
kospi = soup.select_one("#KOSPI_now")   #전체 중 하나를 딱 찝어요
print(kospi.text)
~~~



## 네이버 실시간 검색어 뽑아오기

~~~python
url = "https://www.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
for tag in soup.select(".PM_CL_realtimeKeyword_rolling .ah_item"):
    rank = tag.select_one(".ah_r").text
    name = tag.select_one(".ah_k").text
    print(f'{rank}위는 {name}입니다.')
~~~

*`>` 직속자식	 `띄어쓰기 `모든 자식*

*아이디 없어도 독특한 클래스명으로 하면 select 가능*



> **for문**
>
> ~~~python
> a = [0,1,2,3,4]
> b = "easdffgq"
> for i in a:
>     print(a[i],b[i])
> ~~~
>
> ~~~bash
> student@DESKTOP MINGW64 ~/Desktop/TIL/scraping (master)
> $ python currency.py
> 0 e
> 1 a
> 2 s
> 3 d
> 4 f
> ~~~
>
>
>
> ~~~python
> a = [5,1,2,3,4]
> b = "easdffgq"
> for i in a:
>     print(a[i],b[i])
> ~~~
>
> ~~~bash
> student@DESKTOP MINGW64 ~/Desktop/TIL/scraping (master)
> $ python currency.py
> Traceback (most recent call last):
>   File "currency.py", line 15, in <module>
>     print(a[i],b[i])
> IndexError: list index out of range
> ~~~



