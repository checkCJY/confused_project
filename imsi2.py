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
df = pd.read_csv("data.csv")
df['date'] = pd.to_datetime(df['date']) # 날짜 형식 변환 (최초 1회)

# 1. 날짜 입력 (시작/종료일 선택)
date_range = st.date_input("기간 선택", [df['date'].min(), df['date'].max()])

# 출력값 (datetime.date(2025, 1, 1), datetime.date(2025, 1, 13))
st.write(date_range)
if len(date_range) == 2:
    start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    
    # 2. 데이터 필터링 (가장 핵심)
    filter_df = df[df['date'].between(start, end)]

    # 3. 결과 출력 (목록/통계/그래프)
    st.write(f"총 {len(filter_df)}건의 거래", filter_df) # 목록
    st.metric("합계", f"{filter_df['amount'].sum():,}원") # 통계 (금액 컬럼 가정)

    daily_sum = filter_df.groupby('date')['amount'].sum()
    st.line_chart(daily_sum)

#D2

df = pd.read_csv("data.csv")
f_df = f_df = df.copy()
# 1. 입력창 생성
keyword = st.text_input("검색어 입력 (내용 포함)")

# 2. 필터링 (날짜 필터 f_df가 이미 있다고 가정)
if keyword:
    f_df = f_df[f_df['description'].str.contains(keyword, case=False, na=False)]

# 3. 결과 출력 (목록 및 통계)
st.dataframe(f_df)  # 목록
st.metric("검색 결과 합계", f"{f_df['amount'].sum():,}")  # 통계