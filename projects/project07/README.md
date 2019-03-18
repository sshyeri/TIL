~~~
pjt_07
├── crud : 프로젝트 폴더, 루트 디렉토리
│   ├── __init__.py : 해당 디렉토리가 파이썬 모듈로 작동이 가능하도록 해주는 파일
│   ├── settings.py : 설정을 기록해 놓은 파일/언어, 시간, ALLOWED_HOSTS 변수 변경, 메세지 추가
│   ├── urls.py : 루트 url 설정 파일
│   └── wsgi.py
├──movies : 앱 폴더
│   ├── migrations
│   │   ├── 0001_initial.py : genre, movie, score 모델 초기화
│   │   └── __init__.py
│   ├── templates : 템플릿 폴더
│   │   └── movies
│   │       ├── base.html : 부트스트랩 설정 베이스 파일
│   │       ├── details.html : 영화 정보, 평점 정보 보여주는 템플릿
│   │       └── index.html : 영화 목록 보여주는 템플릿
│   ├── __init__.py : 해당 디렉토리가 파이썬 모듈로 작동이 가능하도록 해주는 파일
│   ├── admin.py : 관리자가 접속하면 보이는 화면
│   ├── apps.py : 앱을 등록하는 기능을 하는 파일
│   ├── models.py : genre, movie, score 모델 생성
│   ├── tests.py 
│   ├── urls.py : url연결을 위한 파일
│   └── views.py : 화면 구성을 위한 파일
├── db.sqlite3
├── genre.csv : genre 클래스에 들어갈 데이터
├── movie.csv : movies 클래스에 들어갈 데이터
└── manage.py

~~~

