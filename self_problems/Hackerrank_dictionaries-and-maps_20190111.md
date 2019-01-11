### 입력값 없을 때 까지 출력하기

**[HackerRank_dictionaries-and-maps](https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?isFullScreen=true)**

~~~python
phoneBook = {}
for i in range(int(input())):
    inputstring = input().split()
    phoneBook[inputstring[0]] = inputstring[1]
while True:
    name = input()
    if not name:
        break
    elif name not in phoneBook.keys():
        print('Not found')
    else:
        print(name+'='+phoneBook[name])
~~~

