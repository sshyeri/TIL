### stdin 

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

### str <-> list

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

###  대소문자

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



### pop



### 출력

