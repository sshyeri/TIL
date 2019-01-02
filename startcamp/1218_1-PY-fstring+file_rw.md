# bash

**touch  파일명**		파일 만들기

**code 파일명**			vs**code**에서 파일 실행

**clear(`ctrl`+`l`)**		화면에 쌓인 스크립트 지우기

**cd ~**				홈 위치로 이동

# STRING

~~~python
# pyformat
#'{} {}'.format('one','two')
name = '도레미'
e_name = 'doraemi'
print('안녕하세요? {}입니다. my name is {}.'.format(name, e_name))
print('안녕하세요? {1}입니다. my name is {0}.'.format(name, e_name))
print('안녕하세요? {1}입니다. my name is {1}.'.format(name, e_name),'\n')

# f-string python 3.6
print(f'안녕하세요? {name}입니다. my name is {e_name}')
~~~

> ~~~bash
> student@DESKTOP MINGW64 ~/desktop/TIL (master)
> $ python string_test.py
> 안녕하세요? 도레미입니다. my name is doraemi.
> 안녕하세요? doraemi입니다. my name is 도레미.
> 안녕하세요? doraemi입니다. my name is doraemi.
> 
> 안녕하세요? 도레미입니다. my name is doraemi
> ~~~

*`ctrl`+`/` : 주석처리하기, 블록해서 여러 줄도 가능*



**Lotto 추첨**

~~~python
import random

numbers = range(1,46)
pick = random.sample(numbers, 6)
print(f'추첨 번호는 {sorted(pick)}입니다.')
~~~

> ~~~bash
> student@DESKTOP MINGW64 ~/desktop/TIL (master)
> $ python string_test.py
> 추첨 번호는 [6, 10, 13, 16, 28, 40]입니다.
> ~~~



**출력 연습**

~~~python
name = '도레미'
a=[1,2,3,4]
b=[5,6,7,8,9]
c=range(5)
d=range(4)
#print(a+b+'\n') ----------> error
print(a+b,'\n')
#print(c+d) ---------> error
print(list(c)+list(d))
~~~

> ~~~ bash
> student@DESKTOP MINGW64 ~/Desktop/TIL (master)
> $ python string_test.py
> 추첨 번호는 [15, 20, 21, 24, 25, 37]입니다.
> [1, 2, 3, 4, 5, 6, 7, 8, 9]
> 
> [0, 1, 2, 3, 4, 0, 1, 2, 3]
> 내 이름은도레미
> ~~~





# 파일



## 파일명 바꾸기

[txt 파일 500개 생성](zzu.li/dummy)

1. os를 import!
   - import os

2. 해당 폴더로 들어간다.
   - os.chdir(r'폴더주소') ----->맥은 r삭제

3. 폴더 안에 모든 파일을 돌면서 이름을 바꾼다.
   - os.rename( 현재파일명, 바꿀 파일명 )



**모든 파일명 앞에 SAMSUNG붙이기**

~~~python
import os
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
for filename in os.listdir("."):
    os.rename(filename, "SAMSUNG " + filename)
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUNG ", "SAFFY "))    
~~~

*현재 위치는  "."*



**SAMSUNG -> SSAFY로 바꾸기**

~~~python
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUNG ", "SAFFY "))
~~~



**그냥 바꾸기 **

~~~python
import os
os.chdir(r"C:\Users\student\Desktop\TIL")
os.rename("test.txt","quiz.txt")
~~~



## 파일 만들기(쓰기) "w"

~~~python
f = open("new.txt","w")
f.write("Hello !!!")
f.close()
~~~



**with 구문 이용 **

~~~ python
with open("new.txt","w") as f:
    f.write("안녕하세요")
~~~



## 파일 읽어와서 변수 저장하기 "r"

~~~python
with open("new.txt","r") as f:
    data = f.read()
    print(data)
~~~



## 여러 줄 한번에 쓰기

~~~python
with open("new.txt","w", encoding='utf-8') as f:
    for i in range(1,6):
        data = f'{i}번째 줄입니다.\n'
        f.write(data)
~~~

*for문에서 range 쓰세요. range는 메모리 하나 먹음.*



## 뒤에 덧붙여 쓰기 "a"

~~~python
with open("new.txt","a",  encoding='utf-8') as f :
    f.write("짜잔")
~~~



##  cat으로 터미널에서 바로 확인하기

> ~~~bash
> student@DESKTOP MINGW64 ~/Desktop/TIL/file_rw (master)
> $ python make_txt.py
> 
> student@DESKTOP MINGW64 ~/Desktop/TIL/file_rw (master)
> $ cat new.txt
> 1번째 줄입니다.
> 2번째 줄입니다.
> 3번째 줄입니다.
> 4번째 줄입니다.
> 5번째 줄입니다.
> 짜잔
> ~~~



## 리스트로 입력하기

~~~python
menu = ["카레\n", "육개장\n", "라면\n"]
with open("menu.txt","w", encoding='utf-8') as f :
    f.writelines(menu)
~~~

> ~~~bash
> student@DESKTOP MINGW64 ~/Desktop/TIL/file_rw (master)
> $ python make_txt.py
> 
> student@DESKTOP MINGW64 ~/Desktop/TIL/file_rw (master)
> $ cat menu.txt
> 카레
> 육개장
> 라면
> ~~~

