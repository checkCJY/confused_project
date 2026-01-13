import streamlit as st
import pandas as pd

# 예시 데이터 (DataFrame)
transactions = pd.DataFrame({
    "type": ["income", "income", "income", "expense", "expense"],
   "desc": ["월급", "용돈", "중고거래 수익", "식비", "교통비"],
    "amount": [500000, 120000, 300000, 80000, 200000]
})

    
# ------------------------------
# 계산 로직 (요구사항 2번)
# ------------------------------
def calc_summary(transactions):
    income = transactions[transactions["type"] == "income"]["amount"].sum()
    expense = transactions[transactions["type"] == "expense"]["amount"].sum()
    balance = income - expense
    return income, expense, balance
income, expense, balance = calc_summary(transactions)
# ------------------------------
# 실행
# ------------------------------
  

st.title("💰 요약 통계")

# 요구사항 3번: 한눈에 보기 쉽게 표시
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("총 수입", f"{income:,.0f} 원")

with col2:
    st.metric("총 지출", f"{expense:,.0f} 원")

with col3:
    st.metric("현재 잔액", f"{balance:,.0f} 원")

st.write("### 전체 거래 내역")
st.dataframe(transactions)