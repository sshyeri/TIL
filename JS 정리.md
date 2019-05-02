# 연산자

### 일치 연산자 `===`

- 엄격한 비교
- 메모리의 같은 객체를 가리키고, 같은 타입이고, 값도 같다.
- 일치 연산자를 사용하는 것이 좋다.

### 동등 연산자 `==`

- 형변환 비교
- 메모리의 같은 객체를 가리키거나 같은 값을 갖도록 변환할 수 있다면 비교
- 서로 다른 타입이면 비교하기전에 같은 자료형으로 변환하여 비교(1=="1")
- 골칫거리와 혼란을 야기할 수 있다.



# 호이스팅

>  변수를 선언하지도 않았는데 그 변수에 접근할 수 있다는 특이한 현상 



## `let`  vs  `Var`

##### `let` : 블록 스코프

##### `var` : 함수 스코프

- var 로 선언하면 현재 스코프(유효범위)안이라면 어디서든 사용할 수 있으며, 심지어 선언하기도 전에 사용 할 수 있다.

### 

# 콜백 함수

- ssafy() : 명시적 호출

- 콜백 함수는 특정 이벤트가 발생했을 때 시스템에 의해 호출되는 함수.

- 자바스크립트의 함수는 **일급객체**이다.

  ### 일급 객체

  #### 일급 객체의 3가지 조건

  1. 변수에 담을 수 있어야 한다.
  2.  인자로 전달할 수 있다.
  3.  변환 값(return value)으로 전달할 수 있다.

  ~~~javascript
  //1. 변수 fco에 함수가 저장됨
  const fco = function(){
  //3. return value가 익명 함수
  return n => n + 1 
  }
  //2. fco가 console.log()함수의 인자로 전달됨
  console.log(fco) 
  
  //도전 num_101에 101을 담아야 한다.
  const num_101 = fco()(100)
  
  ~~~

  ### 비동기 처리

  - 콜백 함수는 주로 비동기 처리 모델에서 사용
  - 동기(직렬) / 비동기(병렬)
  - 중간에 로드가 오래 걸리는 함수
  - 브라우저는 스레드가 1개 -> 동기를 비동기로 바꿔보자! : 동시에 처리할 수 있게
  - 단일 스레드가 동시에 처리하는 것 : 비동기 처리 모델

  > 파이썬 에서..
  >
  > ~~~python
  > from time import sleep
  > 
  > # 3초 자는 함수
  > def sleep_3s():
  >     sleep(3)
  >     print('Wake up!')
  > print('start sleeping')
  > sleep_3s() # blocking
  > print('end of program')
  > ~~~

  

- non-blocking: 해당 함수의 시작 이후 종료될 때 까지 기다리지 않고 바로 다음 줄의 코드를 실행하는 것을 의미

- 코드의 실행을 막지 않는다.

  ### 이벤트 루프

  - 시간의 흐름에 따라 코드의 수행을 처리.

  - 그 때마다 JS 엔진을 작동시킨다.

  - 콜백함수가 나타나면 이벤트 루프가 콜백 큐에 넣음. 이 외의 함수들이 콜스택에 들어가고 이벤트루프가 콜 스택이 비워지면 콜백 큐의 함수들을 순차적으로 콜 스택에 넣는다.

  - ![움잘](https://cdn-images-1.medium.com/max/1600/1*TozSrkk92l8ho6d8JxqF_w.gif)

  - [code to gif](<http://latentflip.com/loupe/?code=ZnVuY3Rpb24gcHJpbnRIZWxsbygpIHsNCiAgICBjb25zb2xlLmxvZygnSGVsbG8gZnJvbSBiYXonKTsNCn0NCg0KZnVuY3Rpb24gYmF6KCkgew0KICAgIHNldFRpbWVvdXQocHJpbnRIZWxsbywgMzAwMCk7DQp9DQoNCmZ1bmN0aW9uIGJhcigpIHsNCiAgICBiYXooKTsNCn0NCg0KZnVuY3Rpb24gZm9vKCkgew0KICAgIGJhcigpOw0KfQ0KDQpmb28oKTs%3D!!!PGJ1dHRvbj5DbGljayBtZSE8L2J1dHRvbj4%3D>)

    

# EventListener

- [무엇]을 [언제] [어떻게] 한다.
- 버튼을 클릭하면 [ ]한다.

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div id="my">
    </div>
    <button id="this-button">Click me</button>
    <script>
    /*
        [무엇]을 [언제] [어떻게] 한다.
    */
    //1. 무엇 => 버튼
    const button = document.querySelector('#this-button')

    //2. 언제 => 버튼을 '클릭'하면
    button.addEventListener('click', event => {
        const area = document.querySelector('#my')
        //3. 어떻게 => 뿅한다.
        area.innerHTML = '<h1>뿅</h1>'
    })
    </script>
</body>
</html>
~~~

