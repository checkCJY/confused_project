# 화면 레이아웃, 대시보드 지표, 차트 출력을 담당합니다.import streamlit as st
import streamlit as st

class UIRenderer:
    @staticmethod
    def render_header():
        """앱 제목 출력"""
        st.title("💰 통합 가계부 관리 서비스")

    @staticmethod
    def render_metrics(income, expense, balance):
        """핵심 지표(Metric) 위젯 출력"""
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("총 수입", f"{income:,} 원")
        col_b.metric("총 지출", f"-{expense:,} 원", delta_color="inverse")
        col_c.metric("현재 잔액", f"{balance:,} 원")

    @staticmethod
    def render_budget_status(total_exp):
        """예산 상태 확인 및 프로그레스 바 출력"""
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
                st.warning("⚠️ 예산의 80%를 사용했습니다!")
            else:
                st.success(f"✅ 예산 범위 내 관리 중 (잔여: {budget - total_exp:,.0f}원)")

    @staticmethod
    def render_analysis_charts(df):
        """카테고리별/일별 지출 차트 출력"""
        exp_df = df[df["type"] == "지출"]
        if not exp_df.empty:
            st.write("### 카테고리별 지출")
            st.bar_chart(exp_df.groupby("category")["amount"].sum())
            st.write("### 일별 지출 추이")
            st.line_chart(exp_df.groupby("date")["amount"].sum())
        else:
            st.info("필터링된 범위 내에 지출 내역이 없습니다.")