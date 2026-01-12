# F1

# 화면에 입력 폼을 구성한다:
#     - 날짜 입력창 생성 (st.date_input)
#     - 구분 선택창 생성 (수입/지출, st.selectbox)
#     - 카테고리 선택창 생성 (식비/교통비 등, st.selectbox)
#     - 내용 입력창 생성 (st.text_input)
#     - 금액 입력창 생성 (st.number_input, 정수형태)

# "등록" 버튼이 눌렸는지 확인한다:
#     IF "등록" 버튼이 클릭됨:
#         IF 금액이 0보다 크고 내용이 입력됨 (기본 검증):
#             {날짜, 구분, 카테고리, 내용, 금액}을 묶어 '거래 객체'를 생성한다.
#             생성된 객체를 '거래목록 리스트'의 끝에 추가(append)한다.
#             사용자에게 "등록 완료" 메시지를 표시한다.
#        ELSE (검증 실패 시):
#             "올바른 금액과 내용을 입력해주세요"라고 경고한다.

import streamlit as st

# 1. 데이터 저장 공간 준비 (세션 상태)
if 'history' not in st.session_state:
    st.session_state.history = []

# 2. UI 구성
st.title("가계부 등록 서비스")
date = st.date_input("날짜")
type = st.selectbox("구분", ["지출", "수입"])
category = st.selectbox("카테고리", ["식비", "교통", "쇼핑", "기타"])
content = st.text_input("내용")
amount = st.number_input("금액", step=1)

# 3. 로직 처리
if st.button("등록"):
    if amount > 0:
        new_item = {
            "날짜": date,
            "구분": type,
            "카테고리": category,
            "내용": content,
            "금액": amount
        }
        st.session_state.history.append(new_item)
        st.success("거래가 등록되었습니다!")
    else:
        st.error("금액을 정확히 입력해주세요.")


# 거래목록 조회
#     IF 거래 목록이 비어 있거나 존재하지 않는다면:
#         - 화면에 “등록된 거래가 없습니다.”라는 안내 메시지를 출력한다.

#     ELSE (거래 목록에 데이터가 하나라도 있다면):
#         Python의 Pandas 라이브러리를 사용하여 거래 목록(리스트)을 데이터프레임(DataFrame) 구조로 변환한다.
#         데이터프레임의 컬럼명을 요구사항에 맞춰 설정한다:
#         (날짜, 구분, 카테고리, 내용, 금액)
#         Streamlit의 표 출력 기능(st.dataframe 또는 st.table)을 사용하여 화면에 표를 그린다.

