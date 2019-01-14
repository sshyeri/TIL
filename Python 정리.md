## Tip

 - 잘 모르겠을 때는 [python tutor](http://pythontutor.com/visualize.html#mode=edit)에 visualizing 해보기

## stdin 

​	**표준 입력 함수, sys에 내장.(import sys 필요)**

​		 `read()` : EOF까지 모두 읽기

​		`readline()` : 개행 전 까지 읽기

​		`readlines()` : 개행기준으로 나눠서 리스트로 만들어 리턴

~~~python
import sys
print(sys.stdin.read())

import sys
print(sys.stdin.readline())

import sys
print(sys.stdin.readlines())
~~~

~~~bash
student@DESKTOP MINGW64 ~/Desktop/til (master)
$ python playground.py
1
2
3456
48
^Z
1
2
3456
48

student@DESKTOP MINGW64 ~/Desktop/til (master)
$ python playground.py
1
1

$ python playground.py
1 2 3 4
5
^Z
['1 2 3 4\n', '5\n']
~~~

## str <-> list

~~~python
>>> char = list('hello')
>>> char
['h', 'e', 'l', 'l', 'o']

# string => list
>>> words = "python은 프로그래밍을 배우기에 아주 좋은 언어입니다."
>>> words_list = words.split()
>>> words_list
['python은', '프로그래밍을', '배우기에', '아주', '좋은', '언어입니다.']

>>> time_str = "10:34:17"
>>> time_str.split(':')
['10', '34', '17']

# list => string
>>> time_list
['10', '34', '17']
>>> ':'.join(time_list)
'10:34:17'
~~~

##  대소문자

~~~python
#단어별로 맨 앞 글자 대문자로
s = "Hi, i'm hyeri."
print (s.title())
#-> Hi, I'M Hyeri.

#모든 문자열을 대문자로
print(s.upper())
#-> HI, I'M HYERI.

#모든 문자열을 소문자로
print(s.lower())
#-> hi, i'm hyeri.
~~~



## 재귀

 최대 재귀 깊이가 1,000번

 for문이 더 효율적일 때가 많음

## Class

<wikipedia - 객체지향 프로그래밍>

> 객체 지향 프로그래밍(영어: Object-Oriented Programming, OOP)은 컴퓨터 프 로그래밍의 패러다임의 하나이다. 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있다.
>
> 명령형 프로그래밍인 절차지향 프로그래밍에서 발전된 형태를 나타내며, 기본 구성요소는 다음과 같다.

- **클래스(Class)** - 같은 종류(또는 문제 해결을 위한)의 집단에 속하는 속성(attribute)과 행위(behavior)를 정의한 것으로 객체지향 프로그램의 기본적인 사용자 정의 데이터형(user define data type)이라고 할 수 있다. 클래스는 프로그래머가 아니지만 해결해야 할 문제가 속하는 영역에 종사하는 사람이라면 사용할 수 있고, 다른 클래스 또는 외부 요소와 독립적으로 디자인하여야 한다.

- **인스턴스** - 클래스의 인스턴스(실제로 메모리상에 할당된 것)이다. 객체는 자신 고유의 속성(attribute)을 가지며 클래스에서 정의한 행위(behavior)를 수행할 수 있다. 객체의 행위는 클래스에 정의된 행위에 대한 정의를 공유함으로써 메모리를 경제적으로 사용한다.

- **메서드(Method)** - 클래스로부터 생성된 객체를 사용하는 방법으로서 객체에 명령을 내리는 것이라 할 수 있다. 메서드는 한 객체의 속성을 조작하는 데 사용된다.

####  클래스 객체

```python
class ClassName:
    
```

* 선언과 동시에 클래스 객체가 생성됨.

* 또한, 선언된 공간은 지역 스코프로 사용된다.

* 정의된 어트리뷰트 중 변수는 멤버 변수로 불리운다.

* 정의된 함수(`def`)는 메서드로 불리운다.

~~~python
class Person:
    pass
p = Person()     #instance 생성, p가 Person안의 매서드들에 접근
print(p)
~~~

```
<__main__.Person object at 0x000001ABE8BADD68>
```

~~~python
class Person:
    name = '고길동'
    def sayhello(self):
        print(f"Hello, I'm {self.name}.")
~~~

#### 인스턴스 객체

* 인스턴스 객체는 `ClassName()`을 호출함으로써 선언된다.
* 인스턴스 객체와 클래스 객체는 서로 다른 이름 공간을 가지고 있다.
* 인스턴스 -> 클래스 -> 전역 순으로 탐색을 한다.

~~~python
# iu라는 클래스 Person의 인스턴스를 만들어봅시다. 
iu = Person()
# 인사하는 메서드를 호출해봅시다.
iu.sayhello()
>>> Hello, I'm 고길동.
# iu의 이름을 확인해봅시다.
iu.name
>>> '고길동'
# iu로 이름을 바꿔주세요.
iu.name = 'iu'
iu.name
>>> 'iu'
# iu가 인사를 합니다.
iu.sayhello()
>>> Hello, I'm iu.
# iu와 Person이 같은지 확인해보겠습니다.
isinstance(iu, Person)
>>> True
# iu를 출력해봅시다.
iu
>>> <__main__.Person at 0x1abe8bd37f0>	#객체로 선언
# iu를 출력해봅시다 2.
print(iu)
>>> <__main__.Person object at 0x000001ABE8BD37F0>
# map을 만들어 비교해 봅시다.
map(int, '123')
>>> <map at 0x1abe8c37828>
Person
>>> __main__.Person

~~~



**파이썬이 자주 쓰는 것들의 클래스명은 소문자로. 딱히 규칙성은 없음.**  

~~~python
print(type(a), type(b), type(c))
#a = [] 랑 a = list()랑 같음. 그냥 자주 써서 예외임
~~~

```
<class 'tuple'> <class 'dict'> <class 'list'>
```



**Person 클래스 만들기:**

~~~python
class Person():
    name = '강혜리'
    phone = '010-2084-1695'
    pocket = {}
    def greeting(self):
        print(f'안녕, 나는 {self.name}야 내 번호는 {self.phone}야')
    def get_my_pocket(self):
        print(self.pocket)
    def in_my_pocket(self, thing, n):	#self는 반드시 제일 처음에 쓸 것.
        if self.pocket.get(thing):
            self.pocket[thing] += n
        else:
            self.pocket[thing] = n
        print(f'주머니에 {thing} {n} 추가되었습니다.')
        self.get_my_pocket()			#안의 함수 호출 가능
        return self.pocket
~~~



**인스턴스 생성 시 값이 초기화 될 수 있도록**

~~~python
class Person():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    def greeting(self):
        print(f'안녕하세요. {self.name}입니다. {self.age}살입니다.')
~~~

~~~python
p1 = Person('홍길동', 20)
p1. greeting()
p2 = Person('둘리')
p2.greeting()
~~~

```
안녕하세요. 홍길동입니다. 20살입니다.
안녕하세요. 둘리입니다. 0살입니다.
```



## List

- List는 함수에 넘어갈 때 참조가 아닌 **원본**이 넘어감! (reference 타입들 : 딕셔너리, 셋, 클래스, 객체 등 )
- 