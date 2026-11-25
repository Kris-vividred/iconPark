# iconPark

iconmonstr.com 홈페이지 구조를 참고해 만든 아이콘 라이브러리 홈페이지입니다. 브랜드(iconPark)와 아이콘은 모두 새로 그린 것입니다.

**사이트: https://kris-vividred.github.io/iconPark/**

- 단일 파일: `index.html` (빌드 없음, 외부 의존은 웹폰트뿐: Pretendard(jsDelivr), JetBrains Mono(Google Fonts))
- 보안
  - Content-Security-Policy(meta): 인라인 스크립트는 해시가 등록된 2개만 실행, 외부 스크립트·인라인 이벤트 핸들러 차단, 스타일·폰트는 jsDelivr/Google Fonts만 허용
  - **`index.html`의 `<script>` 내용을 고치면 반드시 `python3 tools/update-csp.py`로 해시를 갱신**해야 합니다(안 하면 스크립트가 실행되지 않음). `--check`로 확인만 할 수 있음
  - Pretendard CSS는 SRI(integrity)로 변조 여부를 확인. Google Fonts CSS는 브라우저마다 내용이 달라 SRI를 걸 수 없음
  - 사용자 입력(검색어)은 이스케이프한 뒤 화면에 넣음
- 아이콘 249개, 9개 컬렉션, 스타일 필터 라인/채움/컬러
  - 기본 세트: 39종 × 라인/채움 = 78개 (24×24, 2px 스트로크)
  - Mono 세트: 71종 130개 (Figma `Icons/Mono` 프레임에서 가져와 32→24 그리드로 변환, id는 `mono-` 접두사). 일부는 한 가지 스타일만 있음 (nav_*, player_*, blank, loading)
  - Color 세트: 41종 (Figma `Icons/Color` 프레임, 48×48 원래 색·그라데이션 그대로 반으로 줄여 24 그리드에 그림, id는 `color-` 접두사). 색상 선택은 적용되지 않음
- 검색 자동완성, 컬렉션·스타일 필터, 페이지네이션
- 상세 창: SVG/PNG 전환, 색상·PNG 크기 선택, SVG·PNG 파일 다운로드, SVG·Base64 코드 복사, 즐겨찾기(localStorage `iconpark-favs`, 예전 키 `monoline-favs`는 자동으로 옮김)
- 애니메이션: 목록에서 아이콘에 마우스를 올리면 한 번 재생. 상세 창 `애니메이션` 탭에서 재생/일시정지·타임라인, 애니메이션 3종(그리기 reveal·눌림 pinch·흔들기 select), 고급 설정(재생 방식 반복/한 번/왕복·지연·속도), 배경색, 애니메이션 SVG(CSS 내장)·GIF·동영상(MP4, 미지원 브라우저는 WebM) 내보내기. 외부 라이브러리 없이 GIF 인코더 내장
- 라이트/다크 모드: 헤더의 Light/Dark 전환 버튼, 선택은 localStorage `iconpark-theme`에 저장 (선택 전에는 기기 설정을 따름)

GitHub Pages로 `main` 브랜치 루트를 배포합니다. `main`에 푸시하면 1분 안팎으로 사이트에 반영됩니다.
