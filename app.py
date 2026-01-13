import streamlit as st
import pandas as pd

st.set_page_config(page_title="Day10 Streamlit", layout="wide")
st.title("🏙️ 프로젝트 시작")
st.write("폴더 생성 → uv 환경 세팅 → 실행 성공까지 완료!")
st.write("이 내용이 보인다면 환경설정 완료!")

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
#카테고리 셀렉박스 수정이 필요해보임 (필수는아님)
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

st.divider() # 화면 구분을 위한 선 추가
st.subheader("📑 거래 목록 조회")

if "history" in st.session_state and len(st.session_state.history) > 0:
    
    # 2. 리스트 데이터를 데이터프레임으로 변환
    # 거래 한 건이 '리스트'이므로, 컬럼 이름을 직접 지정해줘야 합니다.
    df = pd.DataFrame(
        st.session_state.history, 
        columns=["날짜", "구분", "카테고리", "내용", "금액"]
    )

    # 3. 표 출력 (st.dataframe은 인터랙티브한 표, st.table은 고정된 표)
    st.dataframe(df, use_container_width=True)

else:
    # 4. 목록이 비어 있을 때 메시지 출력
    st.info("등록된 거래가 없습니다.")
