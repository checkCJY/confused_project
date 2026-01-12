import streamlit as st
import pandas as pd


# FR-1

st.set_page_config(page_title="Day10 Streamlit", layout="wide")
st.title("🏙️ 프로젝트 시작")
st.write("폴더 생성 → uv 환경 세팅 → 실행 성공까지 완료!")
st.write("이 내용이 보인다면 환경설정 완료!")


st.title("🏙️ FR-1")

# 빈 저장소에 저장하기 위해
if "save_list" not in st.session_state:
    st.session_state.save_list = []

class Transaction:
    def __init__(self, date, ttype, category, description, amount):
        self.date = date          # "2025-01-01"
        self.ttype = ttype        # "지출" 또는 "수입"
        self.category = category    # 카테고리 내용
        self.description = description  # 세부 내용에 대해서
        self.amount = amount    # 가격에 대해서

    # 객체로 생성한 데이터를 리스트 형태로 반환합니다.
    def output(self):
        out_value = [self.date, self.ttype, self.category, self.description, self.amount]
        return out_value

date = st.date_input("날짜를 선택해주세요")
ttype = st.selectbox("수입과 지출중 선택해주세요", ["수입", "지출"])
category = st.text_input("어디에 사용하였는지 입력해주세요")
detail = st.text_input("내용을 입력해주세요", placeholder="예: 점심 식사비용")
value = st.number_input("금액을 입력해주세요", min_value = 0, max_value = 100000000 , step=1)



clicked = st.button("확인")
if clicked:
    # Transaction 객체 생성
    t1 = Transaction(date,ttype,category,detail,value)
    
    # 클래스의 데이터를 리스트로 변환하여 세션 상태 리스트에 추가
    st.session_state.save_list.append(t1.output())
    st.success("등록이 되었습니다!")
    st.dataframe(t1.output())
else:
    if not st.session_state.save_list:
        st.info("아직 등록을 하지 않았습니다.")


df = pd.read_csv("data.csv")
st.dataframe(df)

