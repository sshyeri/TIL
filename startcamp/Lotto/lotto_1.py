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
        print(j.text, end=" ")
    print("+", soup.select_one(" .bonus .ball_645").text,"\n")

