import streamlit as st

class Transaction:
    def __init__(self, date, ttype, category, description, amount):
        self.date = date
        self.ttype = ttype
        self.category = category
        self.description = description
        self.amount = amount

    def output(self):
        return [self.date, self.ttype, self.category, self.description, self.amount]

if 'history' not in st.session_state:
    st.session_state.history = []

st.title("가계부 등록 서비스")
date = st.date_input("날짜")
type = st.selectbox("구분", ["지출", "수입"])
#카테고리 셀렉박스 수정이 필요해보임 (필수는아님)
category = st.selectbox("카테고리", ["식비", "교통", "쇼핑", "기타"])
content = st.text_input("내용")
amount = st.number_input("금액", step=1)

if st.button("등록"):
    if amount > 0:
        transaction_obj = Transaction(
            date.strftime("%Y-%m-%d"), 
            type, 
            category, 
            content, 
            amount
        )
        new_item = transaction_obj.output()
        st.write(new_item)
        st.session_state.history.append(new_item)
        st.success(f"'{content}' 항목이 등록되었습니다!")
    else:
        st.error("금액을 정확히 입력해주세요.")
