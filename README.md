# 🎲 랜덤 역할 분배기 (퉷! 셔플 매칭)

> **공정하고 유쾌한 1:1 무작위 역할 배정 단일 페이지 웹 애플리케이션**  
> 외부 라이브러리 없이 순수 HTML5, CSS3, Vanilla JavaScript만으로 구현된 프로젝트입니다.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-2ea44f?style=for-the-badge&logo=github)](https://ekdha12000-dev.github.io/random-role-assigner/)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/ekdha12000-dev/random-role-assigner)

🔗 **실시간 웹 데모**: [https://ekdha12000-dev.github.io/random-role-assigner/](https://ekdha12000-dev.github.io/random-role-assigner/)


---

## ✨ 핵심 기능 및 특징

1. **단 1가지 정석 무작위 매칭 (Fisher-Yates 1:1 셔플)**
   - 가중치나 편향 없이 공정하게 1:1로 매칭됩니다.
   - 참가자와 역할 수가 다를 경우의 자동 예외 처리:
     - **참가자 > 역할**: 남는 인원은 자동으로 **'대기/서포트'**로 배정.
     - **역할 > 참가자**: 참가자 수에 맞춰 역할을 무작위로 추첨하여 배정.

2. **유쾌한 '퉷!' 롤링 시각 연출**
   - 역할 매칭 시작 시 약 1.8초간의 격렬한 진동(Shake)과 슬롯머신 텍스트 롤링 효과.
   - 캐릭터 입에서 참가자 이름 뱃지가 **'퉷!'** 뿜어져 나와 아래쪽 해당 역할 슬롯 카드에 **"찰칵!(Snap!)"** 착지하는 역동적인 애니메이션.
   - 바쁜 사용자를 위한 **'⏩ 즉시 확인(Skip)'** 기능 지원.

3. **자체 Web Audio API 사운드 신시사이저**
   - 별도 외부 오디오 파일 다운로드 없이 브라우저 내장 오디오 컨텍스트로 실시간 톤을 합성하여 무음원 환경에서도 100% 작동.
   - 롤링 틱틱음, 만화풍 팝 사운드(퉷!), 마린바 코드 착지음, 축하 팡파레 제공. (우측 상단 🔊/🔇 음소거 토글 가능)

4. **결과 공유 & 편의 도구**
   - **📋 결과 복사**: 메신저, 슬랙, 노션 등에 바로 붙여넣기 좋은 서식으로 텍스트 자동 복사.
   - **🔄 다시 뽑기**: 동일 명단으로 즉시 재추첨.
   - **✏️ 명단 수정**: 언제든 입력 화면으로 복귀 (`ESC` 단축키 지원).
   - **단축키 지원**: `Ctrl + Enter` (또는 `Cmd + Enter`)로 즉시 추첨 시작.
   - **빠른 프리셋**: 팀 프로젝트, 스터디/회의, 회식 내기, 보드게임 예시 1초 로드.

---

## 🛠 기술 스택 (Tech Stack)

- **Language**: HTML5, CSS3, Vanilla JavaScript (ES6+)
- **Design**: Clean & Minimal 모던 SaaS 라이트 테마 (Responsive Layout)
- **Audio**: Web Audio API (AudioContext)
- **Effects**: Pure CSS Keyframe Animation, HTML5 Canvas Confetti

---

## 🚀 배포 및 로컬 실행

- **단일 파일 실행**: `index.html` 파일을 더블 클릭하여 웹 브라우저(Chrome, Edge, Whale, Safari 등)에서 즉시 실행 가능합니다.
