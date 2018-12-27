## flask 서버 열어두기, 자동 디버깅

~~~python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
~~~

*맨 뒤에 붙여넣을것*



## Lotto 추첨

~~~python
@app.route("/lotto")
def lotto():
    numbers = list(range(1, 46))
    pick = random.sample(numbers, 6)
    return render_template("lotto.html", pick = pick )
~~~

*lotto.html*

~~~html
<h1>오늘의 추첨번호</h1>
{% for i in pick %}
{{i}}
{% endfor %}
~~~



## 검색 사이트 연동

~~~python
@app.route("/search")
def search():
    return render_template("search.html")
~~~

*search.html*

~~~html
<h1>네이버 검색</h1>
<form action="https://search.naver.com/search.naver">
    <input type="text" name="query"/>
    <input type="submit" value="제출"/>
</form>
<h1>구글검색</h1>
<form action="https://www.google.com/search">
    <input type="text" name="q"/>
    <input type="submit" value="Submit"/>
</form>
<h1>다음검색</h1>
<form action="https://search.daum.net/search">
    <input type="text" name="q"/>
    <input type="submit" value="Submit"/>
</form>
<h1>Yahoo검색</h1>
<form action="https://search.yahoo.com/search">
    <input type="text" name="p"/>
    <input type="submit" value="Submit"/>
</form>
<h1>Youtube검색</h1>
<form action="https://www.youtube.com/results">
    <input type="text" name="search_query"/>
    <input type="submit" value="Submit"/>
</form>
<h1>bing검색</h1>
<form action="https://www.bing.com/search">
    <input type="text" name="q"/>
    <input type="submit" value="Submit"/>
</form>

~~~



## 사이트 핑퐁하기

~~~python
@app.route("/ping")
def ping():
    return render_template("ping.html")

@app.route("/pong")
def pong():
    pingpong = request.args.get('ping')
    return render_template("pong.html", pingpong = pingpong)
~~~

*ping.html*

~~~html
<h1 style="color:brown">핑핑~!~!@@</h1>
<form action = "/pong">
    <input type="text" name="ping"/>
    <input type="submit" value="퐁으로!"/>
</form>
~~~

*pong.htm*

~~~html
<h1 style="color:blue">퐁퐁</h1>
<form action="/ping">
    <input type="text" name="pong"/>
    <input type="submit" value="핑으로!"/>
</form>
~~~



## 롤 티어 검색

~~~python
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/opgg")
def opgg():
    return render_template("opgg.html")
    
@app.route("/tier")
def tier():
    name = request.args.get('userName')
    url = f"http://www.op.gg/summoner/userName={name}"
    req = requests.get(url).text
    soup = BeautifulSoup(req)
    winratio = soup.select_one(" .TierBox .SummonerRatingMedium .winratio")
    tier = soup.select_one(" .TierBox .SummonerRatingMedium .tierRank")
    if winratio:
        return render_template("tier.html", name = name, tier = tier.text, winratio = winratio.text)
    else:
        if tier:
            return render_template("unrank.html", name = name, tier = tier.text)
        else:
            return render_template("none.html", name = name)
~~~



*opgg/html*

~~~html
<h1>아이디를 입력하세요</h1>
<form action="/tier">
    <input type="text" name="userName"/>
    <input type="submit" value="Submit"/>
</form>
~~~

*unrank.html*

~~~html
<h1>{{name}}님은 언랭입니다.</h1>
~~~

*tier.html*

~~~html
<h1>{{name}}님은 {{tier}}, 승률은 {{winratio}}입니다.</h1>
~~~

