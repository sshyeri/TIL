02_web/

1. README.md

2. 01_layout.html
   - Navigation Bar, Header, Footer 포함.
   - 기본 설정: DOCTYPE은 html, 언어는 한국어, 인코딩 설정은 UTF-8, viewport는 width:device-width, initial scale:1.0, title은 영화추천사이트
   - Navigation Bar : Bootstrap의 Navs 컨텐츠 활용. sitcky-top클래스 추가. Iteml 															List에서 Home만 클릭 가능
   - Header : section 클래스 추가-css에서 세부 설정, flex 활용하여 가운데 정렬.
   - Footer : fixed-bottom, px-5, justify-between사용. 화살표 클릭 시 header로 이동.

3. 01_layout.css

   - 구글 폰트 import

   - section 클래스 설정 : 높이 350px,  backgroun-image 삽입, 폰트 설정.
   - Header내부의 h2태그에 가운데 정렬 설정
   - body 폰트 설정.

4. 02_movie.html
   - 01_layout에 movie list 추가.
   - Movie list :  Bootstrap의 card 컨텐츠 활용. 화면크기에 따라 반응형으로 보이는 카드 수 제한. 평점은 badge 컨텐츠활용.

5. 02_movie.css
   - movie list의 subtitle밑에 짧은 밑줄 추가.(shoreline 클래스)

6. 03_detail_view.html
   - movie list이미지 클릭 시 보이는 영화상세정보 추가.
   - movie list의 card와 Bootstrap의 carousel 컨텐츠 연결.

7. 03_detail_view.css
   - header부분의 이미지에 hover 추가.
   - 마우스를 올려 놓았을 때, 이미지 변화.

8. assets/
   - 활용 이미지 폴더

9. abstract-analog-art-390089.jpg
   - header부분의 background 이미지