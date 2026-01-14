# 실행방법
# python3 -m pytest test/test_finance.py 로 실행
import pytest

import pandas as pd

from logic.logic_manager import FinanceLogic, Transaction
from data.constants import COLUMNS, TYPE_INCOME


# 1. 테스트를 위한 공통 데이터(Fixture) 설정
@pytest.fixture
def sample_history():
    return [
        ["2023-01-01", "수입", "급여", "12월 월급", 5000000],
        ["2023-01-05", "지출", "식비", "점심 식사", 12000],
        ["2023-01-10", "지출", "쇼핑", "운동화", 88000],
        ["2023-02-01", "수입", "부수입", "중고판매", 50000],
    ]


@pytest.fixture
def sample_df(sample_history):
    return FinanceLogic.process_dataframe(sample_history)


# 2. Transaction 클래스 테스트
def test_transaction_output():
    test_trans = Transaction("2023-01-01", "수입", "급여", "월급", 5000)
    # 생성된 객체의 리스트 변환 결과가 입력값과 일치하는지 확인
    assert test_trans.output() == ["2023-01-01", "수입", "급여", "월급", 5000]


# 3. FinanceLogic.process_dataframe 테스트
def test_process_dataframe(sample_history):
    df = FinanceLogic.process_dataframe(sample_history)

    # 결과값이 pandas 데이터프레임 형식인지 확인
    assert isinstance(df, pd.DataFrame)
    # 전체 행의 개수가 입력한 4개와 일치하는지 확인
    assert len(df) == 4
    # 'date' 컬럼이 문자열에서 datetime64(날짜 객체) 타입으로 정상 변환되었는지 확인
    assert pd.api.types.is_datetime64_any_dtype(df["date"])
    # 첫 번째 데이터의 금액이 정확히 저장되었는지 확인
    assert df.iloc[0]["amount"] == 5000000


# 4. FinanceLogic.calc_summary 테스트
def test_calc_summary(sample_df):
    income, expense, balance = FinanceLogic.calc_summary(sample_df)

    # 총 수입 합계가 5,050,000원인지 확인 (5,000,000 + 50,000)
    assert income == 5050000
    # 총 지출 합계가 100,000원인지 확인 (12,000 + 88,000)
    assert expense == 100000
    # 순수익(잔액)이 4,950,000원인지 확인 (5,050,000 - 100,000)
    assert balance == 4950000


# 5. FinanceLogic.apply_filters 테스트 (기간 필터)
def test_apply_filters_date(sample_df):
    date_range = ["2023-01-01", "2023-01-31"]
    filtered = FinanceLogic.apply_filters(sample_df, date_range, "")

    # 1월 범위 내 데이터가 3개만 추출되었는지 확인
    assert len(filtered) == 3
    # 필터링된 모든 데이터의 월(month) 정보가 1월인지 확인
    assert all(filtered["date"].dt.month == 1)


# 6. FinanceLogic.apply_filters 테스트 (키워드 필터)
def test_apply_filters_keyword(sample_df):
    filtered = FinanceLogic.apply_filters(sample_df, [], "운동화")

    # '운동화' 키워드가 포함된 행이 1개인지 확인
    assert len(filtered) == 1
    # 필터링된 결과의 설명(description) 필드 내용이 정확한지 확인
    assert filtered.iloc[0]["description"] == "운동화"


# 7. 빈 데이터프레임 처리 테스트 (Edge Case)
def test_calc_summary_empty():
    empty_df = pd.DataFrame(
        columns=["date", "type", "category", "description", "amount"]
    )
    income, expense, balance = FinanceLogic.calc_summary(empty_df)

    # 데이터가 없을 때 수입이 0원인지 확인
    assert income == 0
    # 데이터가 없을 때 지출이 0원인지 확인
    assert expense == 0
    # 데이터가 없을 때 잔액이 0원인지 확인
    assert balance == 0
