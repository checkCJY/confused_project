import streamlit as st
import pandas as pd
import time
from inout import io_manager
from logic import logic_manager
from ui import ui_manager

def main():
    st.set_page_config(page_title="통합 가계부 관리", layout="wide")

    # 객체 초기화
    io = io_manager.IOManager()
    logic = logic_manager.FinanceLogic()
    ui = ui_manager.UIRenderer()
    
    st.title("💰 통합 가계부 서비스")

    # [1] 데이터 로드
    if "history" not in st.session_state:
        st.session_state.history = io.load_transactions()

    # [2] 거래 등록 섹션 (수정됨: submitted 변수 추가)
    submitted, date, ttype, category, content, amount = ui.render_input_form()

    # [수정됨] 버튼 클릭 여부를 submitted 변수로 확인
    if submitted:
        if amount > 0 and content.strip():
            new_item = [date.strftime("%Y-%m-%d"), ttype, category, content, amount]
            
            st.session_state.history.append(new_item)
            io.save_transactions(st.session_state.history)
            
            st.toast("✅ 등록 완료!")
            time.sleep(0.5)
            st.rerun()
        else:
            st.warning("내용과 금액을 정확히 입력해주세요.")

    st.divider()

    # 데이터가 없으면 나온다. 나중에 파일 추가도 만들면 좋을 듯 싶다.
    if not st.session_state.history:
        st.info("데이터를 등록해주세요.")
        st.stop()

    # [3] 데이터 가공 및 필터링
    df_all = logic.process_dataframe(st.session_state.history)
    
    date_range, keyword = ui.render_filter_ui(df_all)
    filter_df = logic.apply_filters(df_all, date_range, keyword)

    # [4] 요약 및 차트 출력
    st.divider()
    ui.render_header()
    
    # 수입, 지출, 잔액을 받고 그 값을 출력
    inc, exp, bal = logic.calc_summary(filter_df)
    ui.render_metrics(inc, exp, bal)
    ui.render_budget_status(exp)

    st.divider()

    # 탭으로 출력
    ui.render_tabs(filter_df)

if __name__ == "__main__":
    main()