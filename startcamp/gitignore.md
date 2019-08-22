*개인 블로그 플랫폼 추천 - **brunch**, medium, selfblog*

## git-CLI

git commit 제외하기

~~~bash
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        test.txt


student@DESKTOP MINGW64 ~/Desktop/TIL (master)
$ touch .gitignore

student@DESKTOP MINGW64 ~/Desktop/TIL (master)
$ ls -al
total 24
drwxr-xr-x 1 student 197121 0 Jan  2 11:23 .
drwxr-xr-x 1 student 197121 0 Jan  2 11:10 ..
drwxr-xr-x 1 student 197121 0 Jan  2 11:22 .git
-rw-r--r-- 1 student 197121 0 Jan  2 11:23 .gitignore
drwxr-xr-x 1 student 197121 0 Jan  2 11:16 baekjoon
drwxr-xr-x 1 student 197121 0 Jan  2 11:16 startcamp
-rw-r--r-- 1 student 197121 0 Jan  2 11:22 test.txt

student@DESKTOP MINGW64 ~/Desktop/TIL (master)
$ echo "test.txt" >> .gitignore

student@DESKTOP MINGW64 ~/Desktop/TIL (master)
$ cat .gitignore
test.txt

student@DESKTOP MINGW64 ~/Desktop/TIL (master)
$ git status
.
.
.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        .gitignore
~~~

*touch .gitignore  :  파일명 앞에 .이 붙으면 숨김파일 생성*

*ls -al  : 숨김파일 까지 모두 확인*

[git ignore 리스트 확인 사이트](https://www.gitignore.io/)



