# GIT

**git add .**				폴더 내 변경사항 모두  add

**git status**			add상황 보기

**ls -al**				모든 파일 보기

**rm -rf  .git**			init 실수 했을 때 잘못된 곳 가서 지우기

---

# PYTHON

**readline()**			한 줄로 읽어서 리턴

**readlines()**			파일 전체를 읽어 list 형태로 리턴\

~~~python
with open("ssafy.txt", "w", encoding='utf=8') as f:
    for i in range(1,11):
        data = f"{i}번째 줄입니다.\n"
        f.write(data)
with open("ssafy.txt","r", encoding='utf=8') as f:
    line = f.readline()
    print(line.strip())
~~~

> ~~~bash
> student@DESKTOP MINGW64 ~/Desktop/TIL (master)
> $ python self.py
> 1번째 줄입니다.
> 
> ~~~



**빈 칸 없애기**

> ~~~bash
> student@DESKTOP MINGW64 ~/Desktop/TIL (master)
> $ python
> Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 13:35:33) [MSC v.1900 64 bit (AMD64)] on win32
> Type "help", "copyright", "credits" or "license" for more information.
> >>> ssafy = "         sdweqq       "
> >>> ssafy.lstrip()
> 'sdweqq       '
> >>> ssafy.rstrip()
> '         sdweqq'
> >>> ssafy.strip()
> 'sdweqq'
> >>>
> ~~~



**추천! 구글 확장프로그램**

> [uBlock Origin](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm/related?hl=ko)  : 광고차단
>
> [Momentum](https://chrome.google.com/webstore/detail/momentum/laookkfknpbbblfpciffpaejjkokdgca) : 뉴탭 예쁘게
>
> [Earth View from google Earth](https://chrome.google.com/webstore/detail/earth-view-from-google-ea/bhloflhklmhfpedakmangadcdofhnnoh/related?hl=ko) : 뉴 탭 구글맵스 사진
>
> [Wappalyzer](https://www.wappalyzer.com/) : 사이트 개발 언어 확인 가능
>
> [octotree](https://chrome.google.com/webstore/detail/octotree/bkhaagjahfmjljalopjnoealnfndnagc) : 왼쪽에 네비게이션처럼
>
> [crxMouse](https://chrome.google.com/webstore/detail/crxmouse-chrome-gestures/jlgkpaicikihijadgifklkbpdajbkhjo) : 윈도우에서 맥처럼 마우스 제스쳐