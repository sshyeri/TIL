## 모바일 증권 문제

```python
import requests
from bs4 import BeautifulSoup

url = "https://m.stock.naver.com/marketindex/index.nhn"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
for tag in soup.select(".international_lst .stock_up"):
    item = tag.select_one(".stock_item").text
    price = tag.select_one(".stock_price").text
    print(item ," : ", price)
```



## 모바일 환율 문제

```python
import requests
from bs4 import BeautifulSoup

url = "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"
req = requests.get(url).text
soup = BeautifulSoup(req,'html.parser')
for tag in soup.select("#asiaBody > table > tbody > tr"):
    name = tag.select_one(".name").text
    idx = tag.select_one(" .idx").text
    print(name, "\t:\t", idx)
```



