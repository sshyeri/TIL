# Git bash

구글 창 열어보기

~~~ bash
student@DESKTOP MINGW64 /
$ python -i
Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 13:35:33) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import webbrowser
>>> webbrowser.open("http://www.google.com")
True
>>> webbrowser.open_new_tab("https://www.google.com")
True
>>>

~~~



# Pyothon_ex

~~~ python

#for문 이용하여 numbers 한 줄 출력
numbers = [2, 3, 6, 8, 11]

for i in numbers:
    print(i, end=" ")


#짝수, 홀수 리스트 만들어 출력
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd = []
even = []

for i in number:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("짝수 :",even)
print("홀수 :",odd)

~~~

~~~ bash
student@DESKTOP MINGW64 ~
$ cd ..

student@DESKTOP MINGW64 /c/Users
$ cd ..

student@DESKTOP MINGW64 /c
$ cd work

student@DESKTOP MINGW64 /c/work
$ python ex_1.py
2 3 6 8 11

짝수 : [2, 4, 6, 8, 10]
홀수 : [1, 3, 5, 7, 9]
~~~



