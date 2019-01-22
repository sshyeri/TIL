## Tip

 - 잘 모르겠을 때는 [python tutor](http://pythontutor.com/visualize.html#mode=edit)에 visualizing 해보기

## 입력 

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

####  한줄에 들어온 값 원하는 대로 집어넣기

~~~python
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
~~~

~~~
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
~~~

~~~python
print(name)
>>> Krishna
print(scores)
>>> [67, 68, 69]
~~~

## float

#### 소수점 이하 몇자리 표현

~~~python
round(3.87901,2)
>>> 3.88
round(3.7, 2)
>>> 3.7
'%.2f'%8.4
>>> '8.40'
'%.10f'%8.7456
>>> '8.7456000000'
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

## String

#### 문자 판별 메소드

~~~python
str.isalnum() 
>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False

str.isalpha()
>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False

str.isdigit()
>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False

str.islower()
>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False

str.isupper()
>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
~~~





####  대소문자

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

#대<->소문자간 변경
print(s.swapcase())
#-> hI, I'M HYERI.
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

#### 클래스 변수 / 인스턴스 변수

- 클래스 변수 : 모든 인스턴스가 공유
- 인스턴스 변수 : 인스턴스별로 각각 가지는 변수

~~~python
class Person:
    population = 0
    
    def __init__(self, name):
        self.name = name
        Person.population += 1
    def greeting(self):
        print(f'{self.name} 입니다. 반가워요.')
~~~

~~~python
me = Person('헤리')
me.name
>>>> '헤리'

friend = Person('남기')
friend.name
>>>> '남기'

Person.population
>>>> 2
me.population
>>>> 2
~~~



#### 정적 메서드 

- 메서드 호출을 인스턴스가 아닌 클래스가 할 수 있도록 구성
- 정적 메소드는 객체가 전달되지 않음.
- 부모 클래스의 클래스 속성값을 가져옴
- @staticmethod 데코레이터에 의해 래핑된 기본 클래스 함수를 덮어쓸 수 없는 '불변의 속성'을 가지게 됨.



#### 클래스 메서드

- 메서드 호출을 인스턴스가 아닌 클래스가 할 수 있도록 구성

- 클래스 메서드는 인자로 클래스를 넘겨줌.

- cls로 넘겨준 클래스 속성값을 가져옴.
- 하위 클래스 상속은 기본 클래스 함수의 효과를 바꿀 수 있음.



#### 추상 메서드

- 동물 - 고양이과 - 호랑이를 생각해볼 것.
- 동물은 너무 추상적이어서 메서드를 정의하지 못하게 함.



*메서드들이 무엇인가.........*

~~~
class 동물
	@staticmethod
	움직인다.			#동물은 무조건 움직여야 됨. 변경 불가

	@classmethod
	다리 네개 동물 클래스 생성
	@classmethod
	다리 두개 동물 클래스 생성 #여러가지 찍어낼 수 있도록. 매번 설정하기 힘듬. 
	
	@abstractmethod
	먹이 설정 함수		#먹이가 무엇인지 무조건 있어야 하지만 동물이 무엇을 							먹는지 자체를 설정할 수는 없음

개과 고양이과 
호랑이 고양이 ..

~~~



### 상속

- 자식 클래스에서는  부모 클래스의 속성과 메소드를 기재하지 않아도 포함됨.
- 메소드 오버라이딩이 가능. 

~~~python
class 부모클래스:
    ~~~~
class 자식클래스(부모클래스):
    ~~~~
~~~

**예시 코드**


~~~python
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
class Student(Person):		#속성들을 굳이 나열해주지 않아도 되지만
    def __init__(self, firstName, lastName, idNumber, scores): 
        self.firstName = firstName	#선언과 함께 속성을 초기화 하고 싶을 
		self.lastName = lastName	#시에는 초기화 함수에 다시 써 줘야 함
		self.idNumber = idNumber
        self.scores = scores
    def calculate(self):
        ave = sum(self.scores)/len(scores)
        if ave >= 90:
            return 'O'
        elif ave >= 80:
            return 'E'
        else:
            return 'T'

s = Student(Heraldo, Memelli, 8135627, [100, 80])	
s.printPerson()				#부모클래스의 메소드 사용 가능
print("Grade:", s.calculate())
~~~

```
Name: Memelli, Heraldo
ID: 8135627
Grade: O
```

#### 메소드 오버라이딩

- 부모 클래스의 메소드를 자식 클래스에서 재정의 
-  부모 클래스의 오버라이딩 된 메소드는 무시되고 자식클래스의 메소드가 수행됨

~~~python
class Student(Person):
    #생략
    def printPerson(self):
        print(f"{self.name}의 등급은 {self.calculate}입니다.")
s.printPerson()	
~~~

~~~
Heraldo의 등급은 O입니다.
~~~

- 부모 메소드 + 자식 메소드도 가능
- `super()` 사용

~~~ python
class Student(Person):
    #생략
    def printPerson(self):
        super().printPerson
        print(f"{self.name}의 등급은 {self.calculate}입니다.")
s.printPerson()	
~~~

~~~
Name: Memelli, Heraldo
ID: 8135627
Grade: O
Heraldo의 등급은 O입니다.
~~~


#### 다중상속

- C#,  Java는 불가능
- C++, 파이썬은 가능
- 상속 개수에는 제한X
- 메소드 중첩 시 먼저 입력된 부모의 메소드를 상속

~~~python
class 부모1:
 ...
class 부모2:
 ...
class 자식(부모1, 부모2):		#메소드 중첩 시 부모1의 메소드 사용
 ...
~~~



## List

- List는 함수에 넘어갈 때 참조가 아닌 **원본**이 넘어감! (reference 타입들 : 딕셔너리, 셋, 클래스, 객체 등 )
- 

## Dict

#### 최대 키/값 얻기

~~~python
my_dict = {'a':10, 'b':30, 'c':25, 'd':30}
max(my_dict.items(), key = lambda x: x[0])
>>>> ('c', 25)
max(my_dict.items(), key = lambda x: x[1])
>>>> ('b', 30)
max(my_dict.items(), key = lambda x: x[1])[0]
>>>> 'b'
key, value = max(my_dict.items(), key = lambda x: x[1])
key
>>> 'b'
value
>>> 30
[x for x,y in my_dict.items() if y==max(my_dict.values())]
>>> ['b', 'd']
~~~

#### 정렬하기

~~~python
x = sorted(my_dict, key=(lambda key : my_dict[key]), reverse=True)
>>> ['b','d','c','a']
~~~






## lambda

- 함수를 딱 한 줄만으로 만들게 해줌

~~~~python
lambda 인자 : 표현식
~~~~

ex) 두 수 곱하기

~~~python
(lambda x, y : x + y)(10, 20)
>>> 30
~~~

- map 에서 사용하기

  ~~~python
  list(map(lambda x: x**2, range(5))
  >>>[0, 1, 2, 4, 9, 16]
  ~~~


- filter

  ~~~python
  list(filter(lambda x: x%2, range(10)))
  >>>[1, 3, 5, 7, 9]
  ~~~

  

## module

### numpy(행렬)

- n차원 배열 객체

#### 생성 함수



#### tranpose(전치)

- 행렬의 인덱스가 바뀌는 변환

![1547536909667](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547536909667.png)

~~~python
import numpy
print([[1,2,3], [4,5,6]])
my_array = numpy.array([[1,2,3], [4,5,6]])
print(my_array)
print(numpy.transpose(my_array))
~~~

~~~
[[1, 2, 3], [4, 5, 6]]
[[1 2 3]
 [4 5 6]]
[[1 4]
 [2 5]
 [3 6]]
~~~

#### flatten(1차원 배열로 변환)

~~~python
import numpy
my_array = numpy.array([[1,2,3], [4,5,6]])
print (my_array.flatten())
>>> [1 2 3 4 5 6]
~~~

#### concatenate(배열 결합)

```python
# axis=0 방향으로 결합, axis 기본값=0
my_array = np.concatenate((a, b))
print(my_array)
>>> [[1, 2, 3],
	[4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]]
    
# axis = 1 방향으로 결합
my_array = np.concatenate((a, b), axis=1)
print(my_array)
>>> [[1, 2, 3], [7, 8, 9], 
     [4, 5, 6], [10, 11, 12]]
```

#### axis





## builtin functions

### hash()



#### 





