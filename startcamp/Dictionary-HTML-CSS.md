[url 길이 줄여주는 사이트](https://zzu.li/)

# PYTHON

## Dictionary

~~~python
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}
print(ssafy["duration"]["semester1"])
print(ssafy["location"][1])
print(ssafy["classes"]["daejeon"]["manager"])
~~~

~~~bash
student@DESKTOP MINGW64 ~/Desktop/TIL (master)
$ python ex.py
6월까지
대전
yoon
~~~



# HTML

- html과 css는 프로그래밍 언어로 분류되지 않아요.

- 조건, 반복을 하지 못해요. 마크업 언어라서 정보를 띄워주는 거에요.
- html은 공백 최소화. 웬만하면 띄어쓰기X

#### 기본 뼈대

~~~html
<!DOCTYPE html>
<html>
    <head>

    </head>
    <body>
    
    </body>
</html>
~~~

### 공부하고 정리하세요

~~~html
<!DOCTYPE html>
<html lang = "en">
    <head><!---바디 전체 통제.설정 넣는 부분..타이틀, 폰트, 템플릿 등등-->
        <meta charset="utf-8">
        <title>헤리의 블로그</title> <!--주소창 위에 탭부분-->
        <link href="https://fonts.googleapis.com/css?family=Staatliches" rel="stylesheet">
    </head> <!--head는 브라우저에 표기되지 않음-->
    <body><!--h1, p의 부모, 부모자식 관계는 탭으로-->
        <h1>Hello HTML</h1><!--한 줄이 요소, html은 요소들의 집합, 태그는 소문자 권장,-->
        안녕하세요
        안녕하세요<br>안녕하세요<!--줄바꿈-->
        <hr><!--기준선, </br>,</hr>도 가능-->
        <img src="https://thought-leadership-production.s3.amazonaws.com/2016/10/28/14/29/18/d9cc4e0b-ba5c-44b6-9b4d-5feffab18b26/tnc_56094809_preview_cropped.jpg" alt="호수"><!------alt는 엑박시 뜨는 메세지, 음성 읽어줌-->
        <p>안녕하세요</p> <!--단락-->
        <p>안녕하세요</p>
        <p id="uniq" class="ssafy daejeon 879 happy-hacking"></p><!--id는 한개 class는 띄어쓰기로 갯수 설정, 갯수 상관 없음-->
    </body>
</html>

~~~



# CSS

- html은 css포함 가능, css는 html없이 불가능

- html은 단순 정보전달, css는 예쁘게

- [selector 사용법](https://www.w3schools.com/cssref/css_selectors.asp)

- css쓰는 방법 3가지

  1. embeded스타일, head에 스타일 태그 넣을 수 잇음


*[color 이름 사이트](http://www.colors.commutercreative.com/grid/)*

~~~html
<!DOCTYPE html>
<html lang = "en">
    <head>
        <link rel="stylesheet" href="style.css"><!--3순위, 외부 파일 링크-->
        <title>헤리의 블로그</title> 
        <link href="https://fonts.googleapis.com/css?family=Staatliches" rel="stylesheet">
        <style>
            /* h1 { color: rosybrown; } embeded styling, 2순위 */
        </style>
    </head>
    <body>     
        <!-- <h1 class="ssafy" style="color: brown; "> inline styling, 1순위 -->
        <h1>Hello HTML</h1> 
        <hr>  
        <!--묶어주는 애. section, nav... -->
        <div class="container">
            <p>안녕하세요</p> 
            <p id="lunch">점심시간이에요</p>
            <p id="dinner">저녁은?</p>
        </div>
        <p>야식 뭐먹지...</p>
        <hr>
        <p class="text-center">Center</p>
        <p class="text-large text-red">Large Red</p>
        <p class="text-center text-large text-blue">Center Large Blue</p>          
    </body>
</html>

~~~

~~~css
/* universial selector 전체 */
.text-center{
    text-align: center;
}
.text-large{
    font-size: 200%;
}
.text-red{
    color: crimson;
}
.text-blue{
    color : darkblue
}
*{
    background: steelblue;

}
h1, p{
    color: white;
} */
#lunch{
    background: lightcoral;
    color: whitesmoke;
}
#dinner{
    color: beige;
}
.container{
    color : red;
} 
/* 아래쪽 설정이 마지막 */

/* h1 { 
    background: rosybrown; 
}
p{
    background: salmon;
    color: whitesmoke;
} */

~~~



[c9 실행](c9.io/login)

