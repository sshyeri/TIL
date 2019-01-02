import requests
import json
from pprint import pprint 
from bs4 import BeautifulSoup
import os

token = os.getenv("TELEGRAM_BOT_TOKEN")
update = requests.get(f"https://api.telegram.org/bot{token}/getUpdates").json()

chat_id = update["result"][0]["message"]["from"]["id"]
method_name = "sendmessage"

kospi_url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
res = requests.get(kospi_url).text
soup = BeautifulSoup(res,'html.parser')
kospi = soup.select_one("#quotient").text
msg = f"실시간 코스피 지수 : {kospi}"
msg_url = f"https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}"

print(msg_url)
print(requests.get(msg_url))