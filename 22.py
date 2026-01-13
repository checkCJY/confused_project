import streamlit as st
# 1. 계산 로직 함수 (요구사항대로 calc_summary 하나로 통합)
def calc_summary(transactions):
    income = 0
    expense = 0
    
    for t in transactions:
        amount = t['amount']
        if amount > 0:
            income += amount      # 수입 합계
        else:
            expense += abs(amount) # 지출 합계 (절댓값으로 더함)
            
    balance = income - expense     # 잔액 계산
    return income, expense, balance
# --- 메인 영역 ---
# 예시 데이터 (실제로는 파일이나 DB에서 가져오게 됩니다)
transactions = [
    {"desc": "월급", "amount": 5000000},
    {"desc": "식비", "amount": -10000},
    {"desc": "커피", "amount": -5000},
    {"desc": "보너스", "amount": 200000}
]# 함수 실행
total_income, total_expense, current_balance = calc_summary(transactions)
# 2. 스트림릿(st)으로 화면에 표시하기
st.title("💰 가계부 요약 통계")
# 보기 좋게 3개의 컬럼으로 나누어 표시
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("총 수입", f"{total_income:,}원")
with col2:
    st.metric("총 지출", f"{total_expense:,}원", delta_color="inverse")
with col3:
    st.metric("현재 잔액", f"{current_balance:,}원")