# iconPark

iconmonstr.com 홈페이지 구조를 참고해 만든 아이콘 라이브러리 홈페이지입니다. 브랜드(iconPark)와 아이콘은 모두 새로 그린 것입니다.

**사이트: https://kris-vividred.github.io/iconPark/**

- 단일 파일: `index.html` (빌드 없음, 외부 의존은 웹폰트뿐: Pretendard(jsDelivr), JetBrains Mono(Google Fonts))
- 보안
  - Content-Security-Policy(meta): 인라인 스크립트는 해시가 등록된 2개만 실행, 외부 스크립트·인라인 이벤트 핸들러 차단, 스타일·폰트는 jsDelivr/Google Fonts만 허용
  - **`index.html`의 `<script>` 내용을 고치면 반드시 `python3 tools/update-csp.py`로 해시를 갱신**해야 합니다(안 하면 스크립트가 실행되지 않음). `--check`로 확인만 할 수 있음
  - Pretendard CSS는 SRI(integrity)로 변조 여부를 확인. Google Fonts CSS는 브라우저마다 내용이 달라 SRI를 걸 수 없음
  - 사용자 입력(검색어)은 이스케이프한 뒤 화면에 넣음
- 아이콘 343개, 9개 컬렉션, 스타일 필터 라인/채움/컬러
  - 기본 세트: 39종 × 라인/채움 = 78개 (24×24, 2px 스트로크)
  - Mono 세트: 71종 125개 (Figma `Icons/Mono` 프레임에서 가져와 32→24 그리드로 변환, id는 `mono-` 접두사). 일부는 한 가지 스타일만 있음 (nav_*, player_*, blank, loading, 브랜드 심볼 5종 — Figma 원본에서 채움 변형을 지워서 라인만 둠)
  - Color 세트: 41종 (Figma `Icons/Color` 프레임, 48×48 원래 색·그라데이션 그대로 반으로 줄여 24 그리드에 그림, id는 `color-` 접두사). 색상 선택은 적용되지 않음
  - Q 세트: 97종 99개 (Figma `[Q][CLIENT] UI Test`의 `icon/*` 컴포넌트, 88×88 원본 좌표를 그대로 두고 24로 축소해 그림, 단색 `#E6E6E6`은 색상 선택이 적용되게 바꿈, `terranColor`만 원래 색). `heartLine`/`heartShape`, `starLine`/`star`는 라인/채움 짝. 가로로 긴 텍스트 배지 `Mystats`는 제외
  - 추가 규칙: 기존 아이콘과 뜻·모양이 비슷해도 스타일이 다르면 추가함(예: Q의 각진 home·search·heart는 기존 아이콘과 별도로 들어감)
  - 모든 아이콘(기본·Mono·Color·Q) 이름은 FS Library Hub(https://library-hub-rosy.vercel.app) 아이콘 에셋 규칙(`assets/icons/<분류>/<lowerCamelCase>.svg`)을 따름. 대응표는 `tools/fs-names.json`(basic·mono·color, hub = 허브에 같은 아이콘이 있어 그 이름 그대로, rule = 허브에 없어 규칙대로 지음). 채움 변형은 `Fill`, 허브가 짝을 정한 아이콘은 그 접미사(`likeOff`/`likeOn`, `bookmarkOff`/`bookmarkOn`, `nav/menuDefault`/`nav/menuSelected`). 다운로드 파일 이름도 이 이름을 씀. 예전 이름(`trash-can`, `course_fullcolor` 등)은 검색 태그로 남겨 두었고, 즐겨찾기 id는 예전 이름 그대로라 저장된 즐겨찾기는 유지됨
- 검색 자동완성, 컬렉션·스타일 필터, 페이지네이션(한 페이지 = 화면 폭에 맞는 열 수 × 4줄, 창 크기가 바뀌면 다시 계산)
- 상세 창: SVG/PNG 전환, 색상·PNG 크기 선택, SVG·PNG 파일 다운로드, SVG·Base64 코드 복사, 즐겨찾기(localStorage `iconpark-favs`, 예전 키 `monoline-favs`는 자동으로 옮김)
- 애니메이션: 목록에서 아이콘에 마우스를 올리면 한 번 재생. 상세 창 `애니메이션` 탭에서 재생/일시정지·타임라인, 애니메이션 3종(그리기 reveal·눌림 pinch·흔들기 select), 고급 설정(재생 방식 반복/한 번/왕복·지연·속도), 배경색, 애니메이션 SVG(CSS 내장)·GIF·동영상(MP4, 미지원 브라우저는 WebM) 내보내기. 외부 라이브러리 없이 GIF 인코더 내장
- 라이선스: 지금은 숨김(하단 메뉴 버튼과 상세 창 안내 문구에 `hidden`). 내용(`INFO.license`)은 남아 있어 `hidden`만 지우면 다시 보임
- 라이트/다크 모드: 헤더의 Light/Dark 전환 버튼, 선택은 localStorage `iconpark-theme`에 저장 (선택 전에는 기기 설정을 따름)

GitHub Pages로 `main` 브랜치 루트를 배포합니다. `main`에 푸시하면 1분 안팎으로 사이트에 반영됩니다.
