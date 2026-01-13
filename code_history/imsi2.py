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

def calc_summary(df):
    income = df[df['type'] == '수입']['amount'].sum()
    expense = df[df['type'] == '지출']['amount'].sum()
    balance = income - expense
    
    return income, expense, balance


if "save_list" not in st.session_state:
    st.session_state.save_list = []


# D1
df = pd.read_csv("../data.csv")
df["date"] = pd.to_datetime(df["date"])  # 날짜 형식 변환 (최초 1회)

# 1. 날짜 입력 (시작/종료일 선택)
date_range = st.date_input("기간 선택", [df["date"].min(), df["date"].max()])

# 출력값 (datetime.date(2025, 1, 1), datetime.date(2025, 1, 13))
st.write(date_range)
if len(date_range) == 2:
    start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])

    # 2. 데이터 필터링 (가장 핵심)
    filter_df = df[df["date"].between(start, end)]

    # 3. 결과 출력 (목록/통계/그래프)
    st.write(f"총 {len(filter_df)}건의 거래", filter_df)  # 목록
    st.metric("합계", f"{filter_df['amount'].sum():,}원")  # 통계 (금액 컬럼 가정)

    daily_sum = filter_df.groupby("date")["amount"].sum()
    st.line_chart(daily_sum)

# D2

df = pd.read_csv("../data.csv")
f_df = f_df = df.copy()
# 1. 입력창 생성
keyword = st.text_input("검색어 입력 (내용 포함)")

# 2. 필터링 (날짜 필터 f_df가 이미 있다고 가정)
if keyword:
    # 조건에 맞는 내용
    # f_df = f_df[f_df['description'].apply(lambda x: keyword.lower() in str(x).lower())]
    # 추가된 내용
    f_df = f_df[f_df["description"].str.contains(keyword, case=False, na=False)]

# 3. 결과 출력 (목록 및 통계)
st.dataframe(f_df)  # 목록
st.metric("검색 결과 합계", f"{f_df['amount'].sum():,}")  # 통계

# D4


# 1. 데이터 로드 및 요약 함수 정의 (가정)
def calc_summary(df):
    # 'type' 컬럼에 '지출'과 '수입'이 있다고 가정하고 지출 합계 계산
    expense_df = df[df["type"] == "지출"]
    return {"지출합계": expense_df["amount"].sum()}


# 임시 데이터 생성 (실제로는 data.csv에서 불러온 f_df 등을 사용하세요)
# df = pd.read_csv("data.csv")

# --- 여기서부터 요청하신 로직입니다 ---

st.subheader("💰 예산 관리 및 알림")

# 1. 예산 입력창
budget = st.number_input("월 예산 입력", min_value=0, step=10000, value=1000000)

# 2. 현재 총 지출액 가져오기 (f_df는 필터링된 데이터)
# 여기서는 예시를 위해 calc_summary 함수를 실행한 결과를 담습니다.
summary = calc_summary(df)
total_expense = summary["지출합계"]



# 3. 예산이 설정되었을 때만 계산 실행 (0으로 나누기 방지)
if budget > 0:
    # 4. 지출 비율 계산
    ratio = total_expense / budget
    st.write(ratio)

    # 5. 시각적 피드백 제공
    st.write(f"📊 현재 예산 사용률: **{ratio:.1%}**")

    # 진행바 표시 (1.0을 넘어가면 에러가 날 수 있으므로 min 처리)
    st.progress(min(ratio, 1.0))

    # 6. 조건에 따른 알림 제어 로직
    if ratio >= 1.0:
        # 예산 초과 시 에러 메시지
        st.error(f"❌ 예산을 초과했습니다! (초과액: {total_expense - budget:,.0f}원)")

    elif ratio >= 0.8:
        # 80% 이상 사용 시 경고 메시지
        st.warning(
            f"⚠️ 예산의 80%를 사용했습니다! 현재 {total_expense:,.0f}원 지출 중입니다."
        )

    else:
        # 안전한 범위일 때 성공 메시지
        st.success(
            f"✅ 예산 범위 내에서 잘 관리하고 있습니다. (잔여: {budget - total_expense:,.0f}원)"
        )

else:
    st.info("💡 월 예산을 입력하면 지출 비율과 알림을 확인할 수 있습니다.")
