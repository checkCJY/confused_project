import streamlit as st
import pandas as pd
import time

from inout import io_manager
from logic import logic_manager
from ui import ui_manager

def main():
    io = io_manager.IOManager()
    logic = logic_manager.FinanceLogic()
    ui = ui_manager.UIRenderer()
    
    st.set_page_config(page_title="통합 가계부 관리", layout="wide")

    # [1] 데이터 로드
    if "history" not in st.session_state:
        st.session_state.history = io.load_transactions()

    st.title("💰 통합 가계부 서비스")

    # [2] 거래 등록 섹션
    date, ttype, category, content, amount = ui.render_input_form()

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
    # filter_col1, filter_col2 = st.columns(2)
    date_range, keyword = ui.render_filter_ui(df_all)
    filter_df = logic.apply_filters(df_all, date_range, keyword)

    # [4] 요약 및 차트 출력
    st.divider()

    inc, exp, bal = logic.calc_summary(filter_df)
    ui.render_metrics(inc, exp, bal)  # UI 클래스 메서드 호출
    ui.render_budget_status(exp)

    st.divider()

    ui.render_tabs(filter_df)

if __name__ == "__main__":
    main()