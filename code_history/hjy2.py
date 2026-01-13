import streamlit as st
import pandas as pd

class FinanceDashboard:
    def __init__(self, transactions: pd.DataFrame):
        """초기화: 거래 데이터 받아서 저장"""
        self.transactions = transactions
        self.income = 0
        self.expense = 0
        self.balance = 0
        self.calculate_summary()

    def calculate_summary(self):
        """총 수입, 총 지출, 잔액 계산"""
        self.income = self.transactions[self.transactions["type"] == "income"]["amount"].sum()
        self.expense = self.transactions[self.transactions["type"] == "expense"]["amount"].sum()
        self.balance = self.income - self.expense

    def display_kpis(self):
        """총 수입, 총 지출, 잔액 KPI를 Streamlit으로 표시"""
        col1, col2, col3 = st.columns(3)
        col1.metric("총 수입", f"{self.income:,.0f} 원")
        col2.metric("총 지출", f"{self.expense:,.0f} 원")
        col3.metric("현재 잔액", f"{self.balance:,.0f} 원")

    def display_transactions(self):
        """거래 내역 테이블 표시"""
        st.write("### 전체 거래 내역")
        st.dataframe(self.transactions)

    def run(self):
        """대시보드 실행"""
        st.title("💰 요약 통계")
        self.display_kpis()
        self.display_transactions()


# ------------------------------
# 실행 예시
# ------------------------------
transactions = pd.DataFrame({
    "type": ["income", "income", "income", "expense", "expense"],
    "desc": ["월급", "용돈", "중고거래 수익", "식비", "교통비"],
    "amount": [500000, 120000, 300000, 80000, 200000]
})

dashboard = FinanceDashboard(transactions)
dashboard.run()