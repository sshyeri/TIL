### 활용한 API

영화진흥위원회 API

네이버 영화 API



### csv 파일 추가 설명

#### boxoffice.csv :

​	영화진흥위원회 API에서 가져온 결과값을 저장.

​	Movie_code : 영화 대표 코드

​	Movie_name: 영화 제목

​	Audience: 누적 관람객 수

​	Date: 해당일 기록

​	10주간 총 43개의 영화가 기록됨.



#### movie.csv:

​	boxoffice.csv파일에서 영화코드를 추출한 후 이를 이용해 영화진흥위원회  API에서 수집한 데이터를 저장.

​	Movie_code : 영화 대표 코드

​	Movie_name: 국문 영화 제목

​	Movie_name_En: 영어 영화 제목

​	Movie_name_Og: 원래 영화 제목

​	Open_date: 개봉연도

​	Show_time: 상영시간

​	Genres: 장르

​	Directors: 감독

​	Watch_grade: 상영등급

​	Actor1~3: 배우 1~3



#### movie_naver.csv:

​	movie.csv파일에서 국문 영화제목을 바탕으로 네이버 영화 검색 API를 통해 수집한 데이터를 저장.

​	Movie_code: 영화 대표 코드

​	Movie_img: 영화 썸네일 이미지의 URL

​	Movie_link: 하이퍼텍스트 link

​	Movie_rating: 유저 평점

