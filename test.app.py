import streamlit as st
import time

from io_manager import IOManager
from logic_manager import FinanceLogic
from ui_manager import UIRenderer

def main():
    # 인스턴스 생성
    io = IOManager()
    logic = FinanceLogic()
    ui = UIRenderer()

    st.set_page_config(page_title="통합 가계부 관리", layout="wide")

    # [1] 데이터 로드
    if "history" not in st.session_state:
        st.session_state.history = io.load_transactions()

    st.title("💰 통합 가계부 서비스")

    # [2] 거래 등록 섹션
    with st.expander("📝 새 거래 등록", expanded=True):
        c1, c2, c3 = st.columns(3)
        date = c1.date_input("날짜")
        ttype = c2.selectbox("구분", ["지출", "수입"])
        category = c3.selectbox("카테고리", ["식비", "교통", "쇼핑", "급여", "기타"])
        content = st.text_input("내용")
        amount = st.number_input("금액", min_value=0, step=1)

        if st.button("등록"):
            if amount > 0 and content.strip():
                new_item = [date.strftime("%Y-%m-%d"), ttype, category, content, amount]
                st.session_state.history.append(new_item)
                io.save_transactions(st.session_state.history)  # 객체 메서드 호출
                st.toast("✅ 등록 완료!")
                time.sleep(1)
                st.rerun()

    if not st.session_state.history:
        st.info("데이터를 등록해주세요.")
        st.stop()

    # [3] 데이터 가공 및 필터링
    df_all = logic.process_dataframe(st.session_state.history)
    st.divider()
    filter_c1, filter_c2 = st.columns(2)
    date_range = filter_c1.date_input("기간", [df_all["date"].min(), df_all["date"].max()])
    keyword = filter_c2.text_input("검색어")

    filter_df = logic.apply_filters(df_all, date_range, keyword)

    # [4] 요약 및 차트 출력
    st.divider()
    inc, exp, bal = logic.calc_summary(filter_df)
    ui.render_metrics(inc, exp, bal)  # UI 클래스 메서드 호출
    ui.render_budget_status(exp)

    st.divider()
    tab1, tab2 = st.tabs(["📑 목록", "📈 분석"])
    with tab1:
        st.dataframe(
            filter_df.sort_values("date", ascending=False), use_container_width=True
        )
    with tab2:
        ui.render_analysis_charts(filter_df)

if __name__ == "__main__":
    main()