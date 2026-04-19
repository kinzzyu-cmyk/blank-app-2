import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="2026 AI-STEAM 융합 패션디자인 역량 분석",
    page_icon="👗",
    layout="wide",
)

# 데이터 로드
df = pd.read_csv('data.csv', encoding='utf-8')

# 종속변수 계산 (주제 1)
df['AI_활용'] = (
    df['15-1. 나는 생성형 AI를 이용해서 새로운 생각이나 아이디어를 만들어낼 수 있다.']
    + df['15-2. 나는   생성형 AI 의 도움으로 독창적인 글이나 이야기를 쓸 수 있다.']
    + df['15-3. 나는 생성형 AI를 사용해 복잡한 문제를 해결하는 새로운 방법을 찾아낼 수 있다.']
) / 3

# 독립변수 계산 (주제 1)
df['창의성'] = (
    df['1-1. 나는 새로운 아이디어를 떠올리는 것을 즐긴다.']
    + df['1-2. 문제 해결시 기존의 방식 외에도 창의적인 방법을 탐색한다.']
    + df['1-3. 나는 기존의 틀에서 벗어나 자유롭게 상상하는 편이다.']
    + df['1-4. 다양한 정보를 융합하여 새로운 아이디어를 만들어 낼 수 있다.']
) / 4

# 문제해결력
df['문제해결력'] = (
    df['3-1. 문제를 해결하기 위해 여러 가지 아이디어를 떠올려 본다.']
    + df['3-2. 스스로 문제를 정의하고, 해결 방향을 설정할 수 있다.']
    + df['3-3. 다양한 해결 방법을 비교한 후 최적의 방안을 선택하려 한다.']
    + df['3-4. 문제 상황에서 포기하지 않고 끝까지 해결하려고 노력한다.']
) / 4

# 디지털 숙련도
df['디지털_숙련도'] = (
    df['4-1. 나는 디자인 소프트웨어(포토샵, 3D CLO 등)를 능숙하게 다룰 수 있다.']
    + df['4-2. 디지털 콘텐츠 제작 역량']
    + df['4-3. 다양한 디지털 플랫폼을 효과적으로 공유하거나 발표할 수 있다.']
    + df['4-4. 디지털 기술을 디자인 아이디어 실현을 위해 창의적으로 응용할 수 있다.']
) / 4

# 독립변수 계산 (주제 2)
df['디지털_윤리'] = (
    df['6-1. SNS나 커뮤니티에 정보를 공유할 때 타인에게 미칠 영향을 생각한다.']
    + df['6-2. 디지털 환경에서의 개인정보 보호와 보안의 중요성을 인식하고 실천한다.']
    + df['6-3. 온라인에서 상대방과 의사소통할 때 예의와 책임감을 가지고 표현한다.']
    + df['6-4. 사이버폭력, 허위정보 등의 문제에 대한 경각심을 가지고 있다.']
) / 4

df['자기관리'] = (
    df['10-1. 내가 관심있는 분야에 대해 알리 위해 노력한다.']
    + df['10-2.나는 내가 해야겠다고 생각하는 일은 스스로 해결할 수 있다.']
    + df['10-3. 내가 겪는 경험들이 나에게 어떤 의미가 있는지 생각해본다.']
    + df['10-4. 어려운 일을 완수하지 못했을 때, 다음 번에 그 일을 할 때는 더 열심히 노력하겠다고 마음먹는다.']
) / 4

# 고숙련 AI 사용자 (주제 2 종속변수)
median_ai = df['AI_활용'].median()
df['고숙련_AI'] = (df['AI_활용'] >= median_ai).astype(int)

df['AI_활용_그룹'] = np.where(
    df['AI_활용'] >= df['AI_활용'].median(), 'AI 활용 상위 50%', 'AI 활용 하위 50%'
)
df['디지털_숙련도_그룹'] = np.where(
    df['디지털_숙련도'] >= df['디지털_숙련도'].median(), '디지털 숙련도 높음', '디지털 숙련도 낮음'
)

st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: 'Nanum Gothic', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 50%, #bfdbfe 100%);
        color: #0f172a;
    }
    .stApp {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 50%, #bfdbfe 100%);
    }
    .hero-card {
        background: rgba(255, 255, 255, 0.95);
        border: 1px solid rgba(148, 163, 184, 0.30);
        border-radius: 24px;
        padding: 28px;
        margin-bottom: 24px;
        color: #0f172a;
    }
    .section-card {
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid rgba(148, 163, 184, 0.20);
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 24px;
        color: #0f172a;
    }
    .divider {
        height: 1px;
        background: rgba(148, 163, 184, 0.30);
        margin: 24px 0;
    }
    .stText, .stMarkdown, .stHeader, .stSubheader, .stDataFrame, .stTable, .stSelectbox, .stSlider {
        color: #0f172a !important;
    }
    .stTable table {
        color: #0f172a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown(
        """
        <div class="hero-card">
            <h1 style="color:#0f172a; margin-bottom: 10px;">👗 2026 AI-STEAM 융합 패션디자인 역량 분석</h1>
            <p style="color:#1f2937; font-size:1.1rem; margin-top:0;">생성형 AI 시대, 의상디자인 전공 학생들에게 가장 필요한 역량은 무엇인가?</p>
            <div style="margin-top:18px; color:#1f2937; line-height:1.8;">
                <p><strong>분석 대상:</strong> 서울디자인고등학교 스마트패션디자인과 학생 (N=32)</p>
                <p><strong>분석 도구:</strong> Google Colab (Python), Streamlit, Scikit-learn, Statsmodels</p>
                <p><strong>연구 배경:</strong> 3D CLO 및 생성형 AI 도입에 따른 메이커 교육(STEAM) 환경에서 학생들의 핵심 성공 요인을 데이터 기반으로 규명함.</p>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-card">
            <h2 style="color:#ffffff; margin-bottom: 8px;">핵심 분석 설계: 변수 설정</h2>
            <p style="color:#cbd5e1; margin-bottom: 14px;">다중선형 회귀와 로지스틱 회귀를 함께 다뤄 두 모델의 목적과 변수 구성을 한눈에 비교합니다.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

comparison_df = pd.DataFrame(
    [
        [
            '다중선형 회귀',
            '연속형 예측',
            'AI_활용',
            '창의성, 문제해결력, 디지털_숙련도',
            'R-squared, 회귀계수',
            '생성형 AI 활용 능력 점수 예측'
        ],
        [
            '로지스틱 회귀',
            '이진 분류',
            '고숙련_AI',
            '디지털_윤리, 자기관리',
            '정확도, 승산비(odds ratio)',
            '고숙련 AI 사용자 여부 분류'
        ],
    ],
    columns=[
        '모델',
        '분석 유형',
        '종속변수',
        '독립변수',
        '평가지표',
        '분석 목표'
    ],
)

st.dataframe(comparison_df.style.set_properties(**{
    'background-color': 'rgba(15, 23, 42, 0.75)',
    'color': '#f8fafc',
    'border': '1px solid rgba(148, 163, 184, 0.12)'
}))

# 탭 메뉴

# 탭 메뉴
tab1, tab2, tab3, tab4 = st.tabs(["데이터 요약", "주제 1", "주제 2", "What if"])

with tab1:
    filtered_df = df.copy()
    st.header("데이터 요약")
    st.write(f"선택된 그룹: **전체** (응답자 {len(filtered_df)}명)")
    st.subheader("기초 통계")
    st.write(filtered_df[['창의성', '문제해결력', '디지털_숙련도', 'AI_활용']].describe().T)
    st.subheader("결측치")
    missing = filtered_df.isna().sum()
    if missing.any():
        st.write(missing[missing > 0])
    else:
        st.write("결측치가 없습니다.")

with tab2:
    filtered_df = df.copy()
    st.header("주제 1: 다중선형 회귀분석")
    st.write("3D 패션 전공 학생들의 창의성 및 디지털 숙련도가 생성형 AI 창의적 활용 능력에 미치는 영향 분석")
    st.write("종속변수: 생성형 AI 활용 능력 (15-1~15-3 평균 점수)")
    st.write("독립변수: 창의성(1번 항목들), 문제해결력(3번 항목들), 디지털 숙련도(4번 항목들)")

    X = filtered_df[['창의성', '문제해결력', '디지털_숙련도']]
    X = sm.add_constant(X)
    y = filtered_df['AI_활용']
    model = sm.OLS(y, X).fit()

    st.write("회귀 분석 결과:")
    result_table = pd.DataFrame({
        '계수': model.params,
        '표준오차': model.bse,
        't값': model.tvalues,
        'p값': model.pvalues,
        '신뢰구간 하한(2.5%)': model.conf_int()[0],
        '신뢰구간 상한(97.5%)': model.conf_int()[1]
    })
    result_table.index = ['절편'] + ['창의성', '문제해결력', '디지털_숙련도']
    st.dataframe(result_table.round(4))
    st.write(f"모델 결정계수 (R-squared): **{model.rsquared:.4f}**, 수정 결정계수 (Adj. R-squared): **{model.rsquared_adj:.4f}**")

    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_df, x='창의성', y='AI_활용', ax=ax)
    ax.set_title('Creativity vs AI Utilization')
    ax.set_xlabel('Creativity')
    ax.set_ylabel('AI Utilization')
    st.pyplot(fig)

with tab3:
    filtered_df = df.copy()
    st.header("주제 2: 로지스틱 회귀분석")
    st.write("디지털 윤리 의식과 자기주도적 학습 태도가 '고숙련 AI 사용자' 여부를 결정짓는가?")
    st.write("종속변수: 고숙련 AI 사용자 여부 (AI 활용 점수 중앙값 이상인 경우 1, 미만인 경우 0)")
    st.write("독립변수: 디지털 윤리(6번 항목), 자기관리 역량(10번 항목)")

    X_log = filtered_df[['디지털_윤리', '자기관리']]
    X_log = sm.add_constant(X_log)
    y_log = filtered_df['고숙련_AI']
    log_model = sm.Logit(y_log, X_log).fit(disp=False)

    result_log = pd.DataFrame({
        '계수': log_model.params,
        '표준오차': log_model.bse,
        'z값': log_model.tvalues,
        'p값': log_model.pvalues,
        '신뢰구간 하한(2.5%)': log_model.conf_int()[0],
        '신뢰구간 상한(97.5%)': log_model.conf_int()[1],
        '승산비(odds ratio)': np.exp(log_model.params)
    })
    result_log.index = ['절편'] + ['디지털_윤리', '자기관리']

    st.write("로지스틱 회귀 결과:")
    st.dataframe(result_log.round(4))
    st.write(f"모델 정확도: **{(log_model.predict(X_log).round() == y_log).mean():.4f}**")

    fig2, ax2 = plt.subplots()
    sns.boxplot(data=filtered_df, x='고숙련_AI', y='디지털_윤리', ax=ax2)
    ax2.set_title('High-skilled AI User vs Digital Ethics')
    ax2.set_xlabel('High-skilled AI User')
    ax2.set_ylabel('Digital Ethics')
    st.pyplot(fig2)

with tab4:
    st.header("실시간 예측 (What-if)")
    st.write("슬라이더로 디지털 숙련도를 조절하며 AI 활용 점수를 예측합니다.")
    
    # 그룹 필터
    group_option = st.selectbox(
        "그룹 필터",
        ["전체", "AI 활용 상위 50%", "AI 활용 하위 50%", "디지털 숙련도 높음", "디지털 숙련도 낮음"]
    )

    if group_option == "전체":
        filtered_df = df.copy()
    elif group_option in ["AI 활용 상위 50%", "AI 활용 하위 50%"]:
        filtered_df = df[df['AI_활용_그룹'] == group_option]
    else:
        filtered_df = df[df['디지털_숙련도_그룹'] == group_option]
    
    digital_input = st.slider(
        "디지털 숙련도 조절",
        min_value=1.0,
        max_value=5.0,
        value=float(filtered_df['디지털_숙련도'].mean()),
        step=0.1
    )
    mean_creativity = filtered_df['창의성'].mean()
    mean_problem = filtered_df['문제해결력'].mean()
    model_input = sm.add_constant(filtered_df[['창의성', '문제해결력', '디지털_숙련도']])
    model_target = filtered_df['AI_활용']
    try:
        model = sm.OLS(model_target, model_input).fit()
        pred_ai = (
            model.params['const']
            + model.params['창의성'] * mean_creativity
            + model.params['문제해결력'] * mean_problem
            + model.params['디지털_숙련도'] * digital_input
        )
        st.write(f"디지털 숙련도: {digital_input:.1f}일 때 예측 AI 활용 점수: **{pred_ai:.3f}**")

        fig3, ax3 = plt.subplots()
        x_values = np.arange(1.0, 5.01, 0.1)
        y_values = (
            model.params['const']
            + model.params['창의성'] * mean_creativity
            + model.params['문제해결력'] * mean_problem
            + model.params['디지털_숙련도'] * x_values
        )
        ax3.plot(x_values, y_values, marker='o', markersize=3)
        ax3.axvline(digital_input, color='red', linestyle='--', label='Current Digital Proficiency')
        ax3.set_xlabel('Digital Proficiency')
        ax3.set_ylabel('Predicted AI Utilization Score')
        ax3.set_title('Predicted AI Utilization Score by Digital Proficiency')
        ax3.legend()
        st.pyplot(fig3)
    except Exception as e:
        st.error(f"모델 학습에 실패했습니다: {str(e)}. 데이터가 부족하거나 문제가 있을 수 있습니다.")
