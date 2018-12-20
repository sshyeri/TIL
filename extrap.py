import requests
from bs4 import BeautifulSoup

url = "https://m.stock.naver.com/marketindex/index.nhn"
req = requests.get(url).text
soup = BeautifulSoup(req,'html.parser')
for tag in soup.select("ul#marketindexLastList > li"): 
    name = tag.select_one(" .stock_item")
    price = tag.select_one(" .stock_price")
    if name: 
        print(name.text, " : ", price.text)
     

    #content > div > div.ct_box.intnl_major_item > ul


