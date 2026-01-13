import streamlit as st

# 거래 데이터를 구조화하기 위한 클래스
class Transaction:
    def __init__(self, date, ttype, category, description, amount):
        self.date = date
        self.ttype = ttype
        self.category = category
        self.description = description
        self.amount = amount

    def output(self):
        """저장 및 분석을 위해 객체 데이터를 리스트 형태로 반환"""
        return [self.date, self.ttype, self.category, self.description, self.amount]

if 'history' not in st.session_state:
    st.session_state.history = [] # 전체 거래 내역을 담을 리스트

st.title("가계부 등록 서비스")

# 입력 필드들을 변수에 할당
date = st.date_input("날짜")
type = st.selectbox("구분", ["지출", "수입"])
category = st.selectbox("카테고리", ["식비", "교통", "쇼핑", "기타"])
content = st.text_input("내용")
amount = st.number_input("금액", step=1)

# 등록 버튼 클릭 시 처리되는 과정
if st.button("등록"):
    if amount > 0:
        # Transaction 클래스의 인스턴스(객체) 생성
        transaction_obj = Transaction(
            date.strftime("%Y-%m-%d"), 
            type, 
            category, 
            content, 
            amount
        )
        # 객체를 리스트 형식으로 변환
        new_item = transaction_obj.output()
        
        # 세션 상태의 히스토리 리스트에 새 데이터 추가
        st.session_state.history.append(new_item)
        st.success(f"'{content}' 항목이 등록되었습니다!")
    else:
        st.error("금액을 정확히 입력해주세요.")
