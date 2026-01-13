import streamlit as st
import pandas as pd

st.set_page_config(page_title="Day10 Streamlit", layout="wide")
st.title("🏙️ 프로젝트 시작")
st.write("폴더 생성 → uv 환경 세팅 → 실행 성공까지 완료!")
st.write("이 내용이 보인다면 환경설정 완료!")


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
    
if "save_list" not in st.session_state:
    st.session_state.save_list = []


# D1
# df = pd.read_csv("data.csv")

# start, end = st.date_input("기간 선택", value=["2025-01-01", "2025-01-13"])

# clicked = st.button("확인")
# # 만약 클릭버튼을 눌러다면
# if clicked:
#     # 필터링을 통해서 기간을 잡는다
#     start_df = df[df['date'] == 'start']
#     end_df = df[df['date'] == 'end']

#     # 이쪽 로직은, start_df 와 end_df 를 이용하여 범위계산을 작동한다
#         # 비교값은 df[df['date']] 인데, 문자열과 문자열끼리 비교가 가능한가?
#         # 문자열을 형변환처리 후에 비교하면 되겠네.
#         # strip, join함수 이용해서 값으로 만들고, 숫자로 바꾸어서 비교처리
#         # for문으로 돌려서 if문으로 맞는 값들만 출력하면 될 것 같다.
#     st.dataframe()
# else:
#     if not st.session_state.save_list:
#         st.info("아직 등록을 하지 않았습니다.")

#D2

df = pd.read_csv("data.csv")
keyword = st.text_input("검색어 입력 (내용 포함)")


# pandas 함수에서 데이터를 추출하는 함수를 찾는다
# 새변수를 만들어서 초기화한다
# 키워드가 같으면 찾은 내용들을 새 변수에 넣어준다. .append() 
# 반복문을 통해 찾은 내용들을 출력한다 
# 시간이 좀 걸릴 문제 옵시디언에 있을거같음

# transactions1은 위에서 읽어온 데이터를 기반으로 하면 될것같다.
if keyword == transactions1[0]["description"].lower():
    st.write(transactions1[0]["description"])