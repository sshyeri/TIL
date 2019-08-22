Python 챗봇   https://dj2.py.hphk.io/bots/88

//Python List

import random

# 1. menu 리스트 만들어보기
menu = ["김밥천국","김밥나라","김가네","스쿨푸드"]
# 2. 점심메뉴 추천하기
choice = random.choice(menu)
print(choice)
----------------------------------------------------------------------
//Python Dictionary

import random

# 1. menu 리스트를 만들어주세요.
menu = ["이화수전통육개장 대전한밭대점", "롱다리 묵은지 김치찜", "응급실국물떡볶이"]
choice = random.choice(menu)
print(choice)

# 2. 번호 딕셔너리를 만들어주세요.
phonebook = {"이화수전통육개장 대전한밭대점": "123", "롱다리 묵은지 김치찜": "456", "응급실국물떡볶이": "789"}

print(phonebook[choice])
----------------------------------------------------------------------
import random

# 1. menu 리스트를 만들어주세요.
menu = ["이화수전통육개장 대전한밭대점", "롱다리 묵은지 김치찜", "응급실국물떡볶이"]
choice = random.choice(menu)
print(choice)

# 2. 번호 딕셔너리를 만들어주세요.
phonebook = {menu[0]: "123", menu[1]: "456",menu[2]: "789"}

print(phonebook[choice])
-----------------------------------------------------------------------
//조건문

if dust>50:
^^^^print("50초과")
elif 조건:
^^^^어랴ㅐㅓ비
else:
^^^^print("50이하")
---------------------------
# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.
if dust>=151:
  print("매우나쁨")
elif dust>=81:
  print("나쁨")
elif dust>=31:
  print("보통")
else:
  print("좋음")
---------------------------------------------------------------------------
//반복

n=0
while n<3:
^^^^print(n)
^^^^n+=1

0
1
2

---------
dust=[59,24,102]
for i in dust:
^^^^print(i)
---------------------------
# 1. 여러번 인사해보기
greeting="안녕하세요!"
print(greeting)
print(greeting)
print(greeting)
print(greeting,"\n")
# 2. 반복문으로 여러번 인사해보기

for i in range(0,5):
  print(greeting)

for i in greeting:
  print(greeting)
--------------------------------------------------------
range()함수

range(0,5)  range(5) 	[0, 1, 2, 3, 4]
range(1,5) 	[1, 2, 3, 4]
range(7,15) 	[7, 8, 9, 10, 11, 12, 13, 14]
--------------------------------------------------------
API . 데이터 (네이버로 로그인하기, op.gg전적 검색등등)
	공공데이터 : data.go.kr
-----------------------------------------------------------
//sum
list = [65, 7, -98, 54, 2]
print(sum(list))
str = "hello world!"
print(str.count('l'))
-------------------------------------------------------------
Python Documentation https://docs.python.org/ko/3/
 	- 내장함수, 외장함수 확인 등
------------------------------------------------




 SORT





sorted() -----> 원본값이 변하지 않음.

-----------------------------------------------------------------------------------------------------
CLI 종류
	1. 유닉스(shell(sh, zsh, bash 등)
	2. CP/M
	3. DOS의 command.com

bash 명령어 기초
	ls		현재 디렉토리의 내용들을 나열
	cd		현재 작업하는 디렉토리를 변경
	mkdir 	새로운 디렉토리 생성
	echo 	문자열 출력
	rm		파일 지우기(디렉토리 지우기랑 다름)
	exit		터미널 종료

chocolatey!!!윈도우
-->동일 IP 5개 이상 설치시 블랙
Gitforwindows
 Homebrew 맥******






텍스트 편집기	https://www.sublimetext.com/
				vscode ******
				atom
https://www.markdownguide.org/basic-syntax
https://typora.io/

CLI 에서는 항상 자신이 어디에 있는지!!!!






