import streamlit as st
import pandas as pd
import os
from datetime import datetime

# --- [1. 기본 설정 및 클래스 정의] ---
st.set_page_config(page_title="통합 가계부 관리", layout="wide")

class Transaction:
    def __init__(self, date, ttype, category, description, amount):
        self.date = date
        self.ttype = ttype
        self.category = category
        self.description = description
        self.amount = amount

    def output(self):
        return [self.date, self.ttype, self.category, self.description, self.amount]

# --- [2. 데이터 관리 함수] ---
def save_transactions(transactions):
    """CSV 파일 저장"""
    df = pd.DataFrame(transactions, columns=["date", "type", "category", "description", "amount"])
    df.to_csv("data.csv", index=False, encoding="utf-8-sig")

def load_transactions():
    """CSV 파일 로드"""
    if os.path.exists("data.csv"):
        try:
            df = pd.read_csv("data.csv", encoding="utf-8-sig")
            if df.empty: return []
            return df[["date", "type", "category", "description", "amount"]].values.tolist()
        except Exception as e:
            st.error(f"데이터 로드 오류: {e}")
            return []
    return []

def calc_summary(transactions_df):
    """수입, 지출, 잔액 계산 (데이터프레임 기준)"""
    income = transactions_df[transactions_df['type'] == '수입']['amount'].sum()
    expense = transactions_df[transactions_df['type'] == '지출']['amount'].sum()
    balance = income - expense
    return income, expense, balance

# --- [3. 초기 데이터 설정] ---
if "history" not in st.session_state:
    st.session_state.history = load_transactions()

st.title("💰 통합 가계부 관리 서비스")

# --- [4. 거래 등록 UI] ---
with st.expander("📝 새 거래 등록하기", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        date = st.date_input("날짜")
    with col2:
        ttype = st.selectbox("구분", ["지출", "수입"])
    with col3:
        category = st.selectbox("카테고리", ["식비", "교통", "쇼핑", "급여", "기타"])
    
    content = st.text_input("내용")
    amount = st.number_input("금액", min_value=0, step=1)

    if st.button("등록"):
        if amount > 0 and content.strip():
            new_item = Transaction(date.strftime("%Y-%m-%d"), ttype, category, content, amount).output()
            st.session_state.history.append(new_item)
            save_transactions(st.session_state.history)
            st.success(f"'{content}' 등록 완료!")
            st.rerun()
        else:
            st.error("금액과 내용을 확인해주세요.")

# 데이터가 없을 경우 처리
if not st.session_state.history:
    st.info("등록된 데이터가 없습니다. 먼저 거래를 등록해주세요.")
    st.stop()

# 전체 데이터를 데이터프레임으로 변환
df_all = pd.DataFrame(st.session_state.history, columns=["date", "type", "category", "description", "amount"])
df_all["date"] = pd.to_datetime(df_all["date"])

# --- [5. 기간 및 키워드 필터 (imsi2 로직)] ---
st.divider()
st.subheader("🔍 데이터 상세 필터")
c1, c2 = st.columns(2)

with c1:
    date_range = st.date_input("기간 선택", [df_all["date"].min(), df_all["date"].max()])
with c2:
    keyword = st.text_input("검색어 입력 (내용 포함)")

# 필터링 적용
f_df = df_all.copy()
if len(date_range) == 2:
    f_df = f_df[f_df["date"].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1]))]
if keyword:
    f_df = f_df[f_df["description"].str.contains(keyword, case=False, na=False)]

# --- [6. 요약 통계 및 예산 알림 (D4 로직)] ---
st.divider()
total_inc, total_exp, balance = calc_summary(f_df)

col_a, col_b, col_c = st.columns(3)
col_a.metric("총 수입", f"{total_inc:,} 원")
col_b.metric("총 지출", f"-{total_exp:,} 원", delta_color="inverse")
col_c.metric("현재 잔액", f"{balance:,} 원")

# 예산 관리 섹션
st.write("---")
st.subheader("🏁 예산 상태 확인")
budget = st.number_input("월 예산 설정", min_value=0, step=10000, value=1000000)

if budget > 0:
    ratio = total_exp / budget
    st.write(f"📊 예산 사용률: **{ratio:.1%}**")
    st.progress(min(ratio, 1.0))

    if ratio >= 1.0:
        st.error(f"❌ 예산을 초과했습니다! (초과액: {total_exp - budget:,.0f}원)")
    elif ratio >= 0.8:
        st.warning(f"⚠️ 예산의 80%를 사용했습니다!")
    else:
        st.success(f"✅ 예산 범위 내에서 잘 관리하고 있습니다. (잔여: {budget - total_exp:,.0f}원)")

# --- [7. 목록 및 시각화] ---
st.divider()
tab1, tab2 = st.tabs(["📑 거래 목록", "📈 지출 분석"])

with tab1:
    st.dataframe(f_df.sort_values("date", ascending=False), use_container_width=True)

with tab2:
    exp_df = f_df[f_df["type"] == "지출"]
    if not exp_df.empty:
        # 카테고리별 차트
        st.write("### 카테고리별 지출")
        cat_sum = exp_df.groupby("category")["amount"].sum()
        st.bar_chart(cat_sum)
        
        # 날짜별 추이 차트
        st.write("### 일별 지출 추이")
        daily_sum = exp_df.groupby("date")["amount"].sum()
        st.line_chart(daily_sum)
    else:
        st.info("필터링된 범위 내에 지출 내역이 없습니다.")
