### HTTP와 HTTPS

HTTPS는 HTTP의 보안이 강화된 버전이다. / HTTP + Secure

SSL(Secure Sockey Layer) 프로토콜을 이용. 데이터를 공개키 방식을 통해 암호화하고 인증의 방식을 통해 보안성을 높인 모델이다. 포트번호는 443을 사용한다.

### HTTP 요청 메소드

- GET: 정보를 요청하기 위해 사용(SELECT)
- POST: 정보를 밀어넣기 위해 사용(INSERT)
- PUT: 정보를 업데이트하기 위해 사용(UPDATE)
- DELETE: 정보를 삭제하기 위해 사용(DELETE)
- HEAD: (HTTP)헤더 정보만 요청. 해당 자원이 존재하는지 혹은 서버에 문자기 없는지를 확인하기 위해 사용
- OPTIONS: 웹서버가 지원하는 메서드의 종류를 요청
- TRACE: 클라이언트의 요청을 그대로 반환. echo서비스로 서버 상태를 확인하기 위한 목적으로 주로 사용





## [브라우저 동작 원리](https://d2.naver.com/helloworld/59361)

![웹킷 동작 과정](https://d2.naver.com/content/images/2015/06/helloworld-59361-3.png)



![모질라의 게코 렌더링 엔진 동작 과정(3.6)](https://d2.naver.com/content/images/2015/06/helloworld-59361-4.png)



### DOM repaint

- 위치를 제외한 CSS가 변경될 때 발생
- Render Tree(Layout)에 영향을 주지 않는 bgc, font color 변경시 발생된다.



### DOM reflow

> repaint보다 reflow가 자원소모가 크다.

- 위치와 클래스가 변경될 때, 브라우저 창 크기가 변경될 때도 발생된다.
- Render Tree가 새롭게 재정립되는 과정이다.



### 최소화 방법

1. 인라인 스타일을 지양한다.

2. table-layout:fixed 제외, 테이블 사용을 지양한다.

3. 변경이 자주 일어나는 요소는 Absolute에 배치해 전체노드에서 분리한다.

   > 배치 방법
   >
   > 1. Normal: 문서 안 위치는 유형, 면적에 따라 배치. 랜더트리에서 DOM트리 위치와 동일
   > 2. Float: Normal과 같이 배치된  후 왼쪽 or 오른쪽으로 이동
   > 3. Absolute: DOM트리와 다른 트리에 배치.

4. 스타일 변경은 DOM 구조상 제일 끝단 노드에서 수행한다.
5. 스타일 변경은 한번에 처리한다.
6. 스타일을 최적화 한다.(CSS 최소화)
7. IE의 경우 CSS에서 js 표현식을 쓰지 않는다.
8. position:relative 사용시 주의한다.

**참고 : [edwith_부스트코스:웹 프로그래밍](https://www.edwith.org/boostcourse-web/joinLectures/12952)





