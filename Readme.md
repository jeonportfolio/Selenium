# 세팅 <br/>

- python 버전 3.12.3 <br/>
- `pip install virtualenv`를 통해 가상환경 설치(각 프로젝트마다 라이브러리가 달라 영향을 받지 않게한다.)<br/>
- `python -m virtualenv venv`를 통해 가상환경 폴더를 생성하고 `venv/Scripts/activate`로 활성화<br/>
- 가상환경 실행 후 `pip install selenium`,`pip install chromedriver_autoinstaller`을 통해 라이브러리들 설치<br/>
- 드라이버는 크롬에서 실행<br/>

# 영상 순위 자동화 탐색 프로그램 <br/>

- 검색 URL을 가져와 연결하고 검색어는 변동이 가능하게 query로 받는다.<br/>
- 네이버에서 제공하는 순위 속성인 `data-cr-rank` 사용 <br/>
- 타겟 사이트 링크를 지정하고 `find_element`,`By.CSS_SELECTOR`를 활용하여 해당 링크를 찾는다. <br/>
- while 문으로 해당 엘리먼트에서 `XPATH`를 사용하여 HTML 구조에서 순위 속성 추적 <br/>
- 하위 순위도 추적하기 위해 스크롤 기능 추가(못찾을 경우 try 구문으로 스크롤하고 for문으로 계속 반복)<br/>
- `zip`을 통해 배열형식으로 다양한 검색어와 사이트에서 검색이 가능 <br/>

# 상품 순위 자동화 탐색 프로그램 <br/>

- PC 버전에서는 고유한 값의 판별이 어려워 모바일 버전에서 상품의 id 값을 받음 <br/>
- url에 나와있는 pagingIndex속성을 통해 페이지 이동하고 검색값을 query값으로 활용<br/>
- scrollBy를 사용해 스크롤 기능 사용(for 문으로 5번 반복)<br/>
- CSS_SELECTOR를 통해 타겟 상품 여부 확인(try except로 존재하거나 존재하지 않는 경우 판별)<br/>
- `data-nclick`속성에서 split을 사용해 순위 속성만 추출<br/>
- for문을 통해 못찾을 경우 14페이지까지 탐색<br/>


# 장소 순위 자동화 탐색 프로그램 <br/>

- PC버전에서는 장소의 고유한 셀렉터가 없기 때문에 모바일 버전에서 셀렉터를 찾는다. <br/>
- 장소 url은 위도와 경도가 있기때문에 바로 접속하기는 어렵고 홈에서 검색후 이동한다. <br/>
- 검색어를 쿼리값으로 받은뒤 해당 url로 이동하고 UI의 더보기 탭을 클릭한다. <br/>
- 목록에서 찾으려는 업체의 ID를 기반으로 url을 포맷하여 찾는다. <br/>
- XPATH를 사용해서 li 태그를 찾는다 (li태그가 순위를 나타냄 )<br/>
- 각 요소를 for문으로 돌면서 rank값을 찾음 (광고는 제외해야함 try문을 통해 예외처리)