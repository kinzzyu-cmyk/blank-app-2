import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
df = pd.read_csv('data.csv', encoding='utf-8')

# 종속변수 계산 (주제 1)
df['AI_활용'] = (df['15-1. 나는 생성형 AI를 이용해서 새로운 생각이나 아이디어를 만들어낼 수 있다.'] + 
                 df['15-2. 나는   생성형 AI 의 도움으로 독창적인 글이나 이야기를 쓸 수 있다.'] + 
                 df['15-3. 나는 생성형 AI를 사용해 복잡한 문제를 해결하는 새로운 방법을 찾아낼 수 있다.']) / 3

# 독립변수 계산 (주제 1)
df['창의성'] = (df['1-1. 나는 새로운 아이디어를 떠올리는 것을 즐긴다.'] + 
                df['1-2. 문제 해결시 기존의 방식 외에도 창의적인 방법을 탐색한다.'] + 
                df['1-3. 나는 기존의 틀에서 벗어나 자유롭게 상상하는 편이다.'] + 
                df['1-4. 다양한 정보를 융합하여 새로운 아이디어를 만들어 낼 수 있다.']) / 4

df['문제해결력'] = (df['3-1. 문제를 해결하기 위해 여러 가지 아이디어를 떠올려 본다.'] + 
                    df['3-2. 스스로 문제를 정의하고, 해결 방향을 설정할 수 있다.'] + 
                    df['3-3. 다양한 해결 방법을 비교한 후 최적의 방안을 선택하려 한다.'] + 
                    df['3-4. 문제 상황에서 포기하지 않고 끝까지 해결하려고 노력한다.']) / 4

df['디지털_숙련도'] = (df['4-1. 나는 디자인 소프트웨어(포토샵, 3D CLO 등)를 능숙하게 다룰 수 있다.'] + 
                       df['4-2. 디지털 콘텐츠 제작 역량'] + 
                       df['4-3. 다양한 디지털 플랫폼을 효과적으로 공유하거나 발표할 수 있다.'] + 
                       df['4-4. 디지털 기술을 디자인 아이디어 실현을 위해 창의적으로 응용할 수 있다.']) / 4

# 독립변수 계산 (주제 2)
df['디지털_윤리'] = (df['6-1. SNS나 커뮤니티에 정보를 공유할 때 타인에게 미칠 영향을 생각한다.'] + 
                     df['6-2. 디지털 환경에서의 개인정보 보호와 보안의 중요성을 인식하고 실천한다.'] + 
                     df['6-3. 온라인에서 상대방과 의사소통할 때 예의와 책임감을 가지고 표현한다.'] + 
                     df['6-4. 사이버폭력, 허위정보 등의 문제에 대한 경각심을 가지고 있다.']) / 4

df['자기관리'] = (df['10-1. 내가 관심있는 분야에 대해 알리 위해 노력한다.'] + 
                  df['10-2.나는 내가 해야겠다고 생각하는 일은 스스로 해결할 수 있다.'] + 
                  df['10-3. 내가 겪는 경험들이 나에게 어떤 의미가 있는지 생각해본다.'] + 
                  df['10-4. 어려운 일을 완수하지 못했을 때, 다음 번에 그 일을 할 때는 더 열심히 노력하겠다고 마음먹는다.']) / 4

# 고숙련 AI 사용자 (주제 2 종속변수)
median_ai = df['AI_활용'].median()
df['고숙련_AI'] = (df['AI_활용'] >= median_ai).astype(int)

# Streamlit 앱
st.title("2026 3D패션 학생 역량 분석 웹페이지")
st.write("어떤 역량이 학생들의 생성형 AI 활용 능력에 영향을 주는가?")

# 데이터 요약
st.header("데이터 요약")
st.write(f"총 응답자 수: {len(df)}")
st.write("AI 활용 능력 평균:", df['AI_활용'].mean())
st.write("고숙련 AI 사용자 비율:", df['고숙련_AI'].mean())

# 주제 1: 다중선형 회귀분석
st.header("주제 1: 다중선형 회귀분석")
st.write("3D 패션 전공 학생들의 창의성 및 디지털 숙련도가 생성형 AI 창의적 활용 능력에 미치는 영향 분석")
st.write("종속변수: 생성형 AI 활용 능력 (15-1~15-3 평균 점수)")
st.write("독립변수: 창의성(1번 항목들), 문제해결력(3번 항목들), 디지털 숙련도(4번 항목들)")

X = df[['창의성', '문제해결력', '디지털_숙련도']]
X = sm.add_constant(X)
y = df['AI_활용']
model = sm.OLS(y, X).fit()

st.write("회귀 분석 결과:")
st.text(model.summary())

# 시각화: 산점도
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='창의성', y='AI_활용', ax=ax)
ax.set_title('Creativity vs AI Utilization Ability')
st.pyplot(fig)

# 주제 2: 로지스틱 회귀분석
st.header("주제 2: 로지스틱 회귀분석")
st.write("디지털 윤리 의식과 자기주도적 학습 태도가 '고숙련 AI 사용자' 여부를 결정짓는가?")
st.write("종속변수: 고숙련 AI 사용자 여부 (AI 활용 점수 중앙값 이상인 경우 1, 미만인 경우 0)")
st.write("독립변수: 디지털 윤리(6번 항목), 자기관리 역량(10번 항목)")

X_log = df[['디지털_윤리', '자기관리']]
y_log = df['고숙련_AI']
log_model = LogisticRegression()
log_model.fit(X_log, y_log)

st.write("로지스틱 회귀 결과:")
st.write(f"계수: {log_model.coef_}")
st.write(f"절편: {log_model.intercept_}")
st.write(f"정확도: {log_model.score(X_log, y_log)}")

# 시각화: 박스플롯
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='고숙련_AI', y='디지털_윤리', ax=ax2)
ax2.set_title('High-Skilled AI User vs Digital Ethics')
st.pyplot(fig2)
