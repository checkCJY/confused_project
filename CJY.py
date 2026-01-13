import streamlit as st
import pandas as pd


# FR-1

# st.set_page_config(page_title="Day10 Streamlit", layout="wide")
# st.title("🏙️ 프로젝트 시작")
# st.write("폴더 생성 → uv 환경 세팅 → 실행 성공까지 완료!")
# st.write("이 내용이 보인다면 환경설정 완료!")


# st.title("🏙️ FR-1")

# # 빈 저장소에 저장하기 위해
# if "save_list" not in st.session_state:
#     st.session_state.save_list = []

# class Transaction:
#     def __init__(self, date, ttype, category, description, amount):
#         self.date = date          # "2025-01-01"
#         self.ttype = ttype        # "지출" 또는 "수입"
#         self.category = category    # 카테고리 내용
#         self.description = description  # 세부 내용에 대해서
#         self.amount = amount    # 가격에 대해서

#     # 객체로 생성한 데이터를 리스트 형태로 반환합니다.
#     def output(self):
#         out_value = [self.date, self.ttype, self.category, self.description, self.amount]
#         return out_value

# date = st.date_input("날짜를 선택해주세요")
# ttype = st.selectbox("수입과 지출중 선택해주세요", ["수입", "지출"])
# category = st.text_input("어디에 사용하였는지 입력해주세요")
# detail = st.text_input("내용을 입력해주세요", placeholder="예: 점심 식사비용")
# value = st.number_input("금액을 입력해주세요", min_value = 0, max_value = 100000000 , step=1)



# clicked = st.button("확인")
# if clicked:
#     # Transaction 객체 생성
#     t1 = Transaction(date,ttype,category,detail,value)
    
#     # 클래스의 데이터를 리스트로 변환하여 세션 상태 리스트에 추가
#     st.session_state.save_list.append(t1.output())
#     st.success("등록이 되었습니다!")
#     st.dataframe(t1.output())
# else:
#     if not st.session_state.save_list:
#         st.info("아직 등록을 하지 않았습니다.")


# df = pd.read_csv("data.csv")
# st.dataframe(df)


# FR-2


# st.title("🏙️ FR-2")


# # 1. 파일 읽어오기
# uploaded = pd.read_csv("data.csv")

# # 2. 파일을 읽어오고, 파일이 있을때만 실행
# # None = 공백, 즉 없다 . uplodaded 가 None가 아닐 때.
# if uploaded is not None:
#     st.success("파일 출력 성공")
#     st.dataframe(uploaded)
# else:
#     st.info("등록된 거래가 없습니다.")


# FR-3

# df = pd.read_csv("data.csv")
# st.dataframe(df)
# st.title("🏙️ FR-3")

# # 계산로직 함수 
# st.write('income은 type이 수입인 내용들의 가격에 접근 후 더한다')
# st.write('expense는 type이 지출인 내용들의 가격에 접근 후 더한다')
# st.write('balance는 잔액 계산')


# def calc_summary(df):
#     income = df[df['type'] == '수입']['amount'].sum()
#     expense = df[df['type'] == '지출']['amount'].sum()
#     balance = income - expense
    
#     return income, expense, balance

# income, expense, balance = calc_summary(df)

# # 3. 화면 표시 (st.metric 사용)
# st.subheader("회계 요약 통계")

# # 옵시디언 8번 자료. columns
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.metric(label="총 수입", value=f"{income:,.0f}원")
    
# with col2:
#     st.metric(label="총 지출", value=f"{expense:,.0f}원", delta_color="inverse")
    
# with col3:
#     # 잔액이 0보다 크면 파란색, 작으면 빨간색으로 표시됨
#     st.metric(label="현재 잔액", value=f"{balance:,.0f}원")


# FR-4

st.title("🏙️ FR-4")

DB_FILE = "data_copy.csv"

# 1. 파일 로드 (실패 시 빈 데이터프레임)
def load_data():
    try: return pd.read_csv(DB_FILE)
    except: return pd.DataFrame(columns=['date', 'type', 'category', 'description', 'amount'])

# 2. 세션 상태 초기화
if 'df' not in st.session_state:
    st.session_state.df = load_data()

# 3. 입력 UI
with st.form("entry_form", clear_on_submit=True):
    date = st.date_input("날짜")
    ttype = st.selectbox("구분", ["수입", "지출"])
    category = st.text_input("어디에 사용하였는지 입력해주세요")
    detail = st.text_input("내용을 입력해주세요", placeholder="예: 점심 식사비용")
    value = st.number_input("금액을 입력해주세요", min_value = 0, max_value = 100000000 , step=1)
    if st.form_submit_button("저장"):
        # 데이터 추가 및 저장
        new_row = pd.DataFrame([{"date": date, "type": ttype, "category":category, "description":detail, "amount": value}])
        st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
        st.session_state.df.to_csv(DB_FILE, index=False, encoding='utf-8-sig')
        st.rerun()

# 4. 결과 출력
st.dataframe(st.session_state.df, use_container_width=True)



