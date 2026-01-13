import streamlit as st
import pandas as pd
import os

class Transaction:
    def __init__(self, date, ttype, category, description, amount):
        self.date = date
        self.ttype = ttype
        self.category = category
        self.description = description
        self.amount = amount

    def output(self):
        return [self.date, self.ttype, self.category, self.description, self.amount]

def save_transactions(transactions):
    """거래 리스트를 CSV 파일로 저장"""
    df = pd.DataFrame(transactions, columns=["date", "type", "category", "description", "amount"])
    df.to_csv(FILE_NAME, index=False, encoding='utf-8-sig')

def load_transactions():
    """CSV 파일에서 거래 내역 로드"""
    if os.path.exists(FILE_NAME):
        try:
            df = pd.read_csv(FILE_NAME, encoding='utf-8-sig')
            if df.empty:
                return []
            df.columns = df.columns.str.strip()
            expected_columns = ["date", "type", "category", "description", "amount"]
            return df[expected_columns].values.tolist()
        except Exception as e:
            st.error(f"데이터 로드 오류: {e}")
            return []
    return []

def calc_summary(transactions):
    """수입, 지출, 잔액 계산"""
    income = 0
    expense = 0
    for item in transactions:
        if item[1] == "수입":
            income += item[4]
        elif item[1] == "지출":
            expense += item[4]
    balance = income - expense
    return income, expense, balance


# --- [메인 앱 구성] ---

# 1. 초기 데이터 설정
if 'history' not in st.session_state:
    st.session_state.history = load_transactions()

st.title("💰 가계부 관리 서비스")

# 2. [F1] 거래 등록 UI
st.subheader("📝 거래 등록")
date = st.date_input("날짜")
ttype = st.selectbox("구분", ["지출", "수입"])
category = st.selectbox("카테고리", ["식비", "교통", "쇼핑", "급여", "기타"])
content = st.text_input("내용")
amount = st.number_input("금액", step=1)

if st.button("등록"):
    if amount > 0 and content.strip():
        # 객체 생성 및 리스트 변환
        transaction_obj = Transaction(
            date.strftime("%Y-%m-%d"), 
            ttype, 
            category, 
            content, 
            amount
        )
        new_item = transaction_obj.output()
        
        # 데이터 추가 및 저장
        st.session_state.history.append(new_item)
        save_transactions(st.session_state.history)
        
        st.success(f"'{content}' 등록 완료!")
        st.rerun() # 화면 갱신
    else:
        st.error("올바른 금액과 내용을 입력해주세요.")

# 3. [F3] 요약 통계 UI
st.divider()
st.subheader("📊 요약 통계")
if st.session_state.history:
    total_inc, total_exp, balance = calc_summary(st.session_state.history)
    col1, col2, col3 = st.columns(3)
    col1.metric("총 수입", f"{total_inc:,} 원")
    col2.metric("총 지출", f"-{total_exp:,} 원", delta_color="inverse")
    col3.metric("현재 잔액", f"{balance:,} 원")
else:
    st.info("통계를 계산할 데이터가 없습니다.")

# 4. [F5] 카테고리별 지출 분석 (그래프)
st.divider()
st.subheader("📈 카테고리별 지출 분석")
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history, columns=["날짜", "구분", "카테고리", "내용", "금액"])
    expense_df = df[df["구분"] == "지출"]
    
    if not expense_df.empty:
        category_sum = expense_df.groupby("카테고리", as_index=False)["금액"].sum()
        st.bar_chart(data=category_sum, x="카테고리", y="금액")
    else:
        st.info("지출 내역이 없습니다.")

# 5. [F2] 거래 목록 조회 UI
st.divider()
st.subheader("📑 거래 목록 상세")
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history, columns=["날짜", "구분", "카테고리", "내용", "금액"])
    st.dataframe(df, use_container_width=True)
else:
    st.info("등록된 거래가 없습니다.")