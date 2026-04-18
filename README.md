# 2026 3D패션 학생 역량 분석 웹페이지

이 웹페이지는 3D 패션 전공 학생들의 역량이 생성형 AI 활용 능력에 미치는 영향을 분석합니다.

## 분석 주제

### 주제 1: 다중선형 회귀분석
3D 패션 전공 학생들의 창의성 및 디지털 숙련도가 생성형 AI 창의적 활용 능력에 미치는 영향 분석

- **종속변수**: 생성형 AI 활용 능력 (설문 15-1~15-3 평균 점수)
- **독립변수**: 창의성(1번 항목들), 문제해결력(3번 항목들), 디지털 숙련도(4번 항목들)

### 주제 2: 로지스틱 회귀분석
디지털 윤리 의식과 자기주도적 학습 태도가 '고숙련 AI 사용자' 여부를 결정짓는가?

- **종속변수**: 고숙련 AI 사용자 여부 (AI 활용 점수 중앙값 이상인 경우 1, 미만인 경우 0)
- **독립변수**: 디지털 윤리(6번 항목), 자기관리 역량(10번 항목)

## 실행 방법

1. 현재 Python 환경에서 필요한 패키지를 설치합니다.

   ```bash
   python3 -m pip install -r requirements.txt
   ```

2. 앱을 실행합니다.

   ```bash
   streamlit run streamlit_app.py
   ```

## GitHub에 반영하는 방법

1. 변경된 파일 상태 확인:

   ```bash
   git status
   ```

2. `requirements.txt` 수정 사항을 스테이징:

   ```bash
   git add requirements.txt
   ```

3. 커밋 생성:

   ```bash
   git commit -m "Pin dependencies and ensure matplotlib is installed"
   ```

4. 원격 저장소로 푸시:

   ```bash
   git push origin main
   ```

> 배포 환경에서는 GitHub에 푸시된 후 자동으로 `requirements.txt`를 다시 설치하므로 `matplotlib` 의존성이 반영됩니다.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)
