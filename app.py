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

if 'history' not in st.session_state:
    st.session_state.history = [] # 전체 거래 내역을 담을 리스트

st.title("✅ FR-01 기능")

# 입력 필드들을 변수에 할당
date = st.date_input("날짜")
type = st.selectbox("구분", ["지출", "수입"])
category = st.text_input("카테고리", placeholder="예시 : 식사")
content = st.text_input("내용", placeholder="예시 : 점심, 또는 간식")
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

st.title("✅ FR-02 기능")


# 1. 파일 읽어오기
uploaded = pd.read_csv("data.csv")

# 2. 파일을 읽어오고, 파일이 있을때만 실행
# None = 공백, 즉 없다 . uplodaded 가 None가 아닐 때.

# 파일 업로드 관련해서 try-except로 수정하면 좋을 것 같다.
if uploaded is not None:
    st.success("파일 출력 성공")
    st.dataframe(uploaded)
else:
    st.info("등록된 거래가 없습니다.")


st.title("✅ FR-03 기능")

class FinanceDashboard:
    def __init__(self, transactions: pd.DataFrame):
        """초기화: 거래 데이터 받아서 저장"""
        self.transactions = transactions
        self.income = 0
        self.expense = 0
        self.balance = 0
        self.calculate_summary()

    def calculate_summary(self):
        """총 수입, 총 지출, 잔액 계산"""
        self.income = self.transactions[self.transactions["type"] == "income"]["amount"].sum()
        self.expense = self.transactions[self.transactions["type"] == "expense"]["amount"].sum()
        self.balance = self.income - self.expense

    def display_kpis(self):
        """총 수입, 총 지출, 잔액 KPI를 Streamlit으로 표시"""
        col1, col2, col3 = st.columns(3)
        col1.metric("총 수입", f"{self.income:,.0f} 원")
        col2.metric("총 지출", f"{self.expense:,.0f} 원")
        col3.metric("현재 잔액", f"{self.balance:,.0f} 원")

    def display_transactions(self):
        """거래 내역 테이블 표시"""
        st.write("### 전체 거래 내역")
        st.dataframe(self.transactions)

    def run(self):
        """대시보드 실행"""
        st.title("💰 요약 통계")
        self.display_kpis()
        self.display_transactions()


# ------------------------------
# 실행 예시
# ------------------------------
test_fr4 = pd.DataFrame({
    "type": ["income", "income", "income", "expense", "expense"],
    "desc": ["월급", "용돈", "중고거래 수익", "식비", "교통비"],
    "amount": [500000, 120000, 300000, 80000, 200000]
})

dashboard = FinanceDashboard(test_fr4)
dashboard.run()

st.title("✅ FR-03 기능")


DB_FILE = "data_copy.csv"
def load_data():
    try: 
        return pd.read_csv(DB_FILE)
    except: 
        return pd.DataFrame(columns=['date', 'type', 'category', 'description', 'amount'])

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
        data_test = {
            "date": date, 
            "type": ttype, 
            "category":category, 
            "description":detail, 
            "amount": value
            }
        new_row = pd.DataFrame([data_test])
        st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
        st.session_state.df.to_csv(DB_FILE, index=False, encoding='utf-8-sig')
        st.rerun()

# 4. 결과 출력
st.dataframe(st.session_state.df, use_container_width=True)


st.title("✅ FR-05 기능")

# 파일 읽어오기
df = pd.read_csv('data.csv')

# '지출' 데이터만 필터링
expense_df = df[df['type'] == '수입']

# 3. 카테고리별 합계 계산 (그룹화)
# 옵시디언 10번 자료 groupby 검색.
category_stats = expense_df.groupby('category')['amount'].sum()

# 표와 막대기 형식으로 보기
st.write(category_stats)
st.bar_chart(category_stats)