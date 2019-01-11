### flask 실행

~~~bash
student@DESKTOP MINGW64 ~/Desktop/ssafy/Flask
$ code app.py
~~~

*flask.py 실행 금지* 



**고정 픽!**

~~~python
from flask import Flask
app = Flask(__name__)
~~~



### rendering html

- import render_template
- py파일 동일 위치에 templates폴더 생성
- templates폴더 내에 html파일 생성

~~~python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '안녕하세요!!!!'

@app.route('/html')
def html():
    return render_template('chicken.html')
~~~



### image

~~~python
    <html>
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1> 치킨치킨치킨치킨!!!!!!! </h1>
    <img src="이미지 주소", alt = "치킨">
</body>
</html>

~~~



### 진자 조건문

~~~python
@app.route("/dictionary/<string:word>")
def dictionary(word):
    word_dict = {'apple':'사과', 'banana':'바나나', 'orange':'오렌지', 'grape':'포도'}
    return render_template('dict.html', word = word, word_dict = word_dict)
~~~

-> html 파일에서

~~~html
{% if word in word_dict %}
    <h1> {{word}}은(는) {{word_dict[word]}}!</h1>
{% else %}
    <h1> {{word}}은(는) 없는 단어입니다.</h1>
{% endif %}
~~~

