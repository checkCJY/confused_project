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


# D4

변수 budget = Streamlit 숫자_입력창("월 예산 입력", 최소값=0) 
budget = st.number_input("월 예산 입력", min_value=0)

// 2. 현재 총 지출액 가져오기 (이미 계산된 서비스 함수 활용) 
변수 total_expense = calc_summary(거래_목록) 중 '지출합계' 

// 3. 예산이 설정되었을 때만 계산 실행 (0으로 나누기 방지) 
만약 budget 이 0보다 크다면: 
if budget > 0:

	// 4. 지출 비율 계산 
	ratio = total_expense / budget

	// 5. 시각적 피드백 제공 (선택 사항) 
	화면에_표시("현재 예산 사용률: {ratio * 100}%") 
	st.write(f"📊 현재 예산 사용률: {ratio:.1%}")
	진행바_표시(최대 1.0 기준 ratio 값) 
	st.progress(min(ratio, 1.0))

	// 6. 조건에 따른 알림 제어 로직 
	만약 ratio 가 1.0 이상이라면: 
	if ratio >= 1.0:
		에러_메시지_표시("❌ 예산을 초과했습니다!") 
		st.error(f"❌ 예산을 초과했습니다! (초과액: {total_expense - budget:,.0f}원)")

	아니고 만약 ratio 가 0.8 이상이라면: 
	elif ratio >= 0.8:
		경고_메시지_표시("⚠️ 예산의 80%를 사용했습니다!") 
		st.warning(f"⚠️ 예산의 80%를 사용했습니다! 현재 {total_expense:,.0f}원 지출 중입니다.")
		
		그 외의 경우 (안전할 때): 
		else: # 예산 범위 내에서 안전할 때 초록색 성공 메시지 출력 st.success(f"✅ 예산 범위 내에서 잘 관리하고 있습니다. (잔여: {budget - total_expense:,.0f}원)")