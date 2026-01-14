import pytest
import pandas as pd
from logic.logic_manager import Transaction, FinanceLogic  

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
    assert test_trans.output() == ["2023-01-01", "수입", "급여", "월급", 5000]

# 3. FinanceLogic.process_dataframe 테스트
def test_process_dataframe(sample_history):
    df = FinanceLogic.process_dataframe(sample_history)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 4
    assert pd.api.types.is_datetime64_any_dtype(df["date"])  # 날짜 변환 확인
    assert df.iloc[0]["amount"] == 5000000

# 4. FinanceLogic.calc_summary 테스트
def test_calc_summary(sample_df):
    income, expense, balance = FinanceLogic.calc_summary(sample_df)
    
    assert income == 5050000  # 5,000,000 + 50,000
    assert expense == 100000  # 12,000 + 88,000
    assert balance == 4950000

# 5. FinanceLogic.apply_filters 테스트 (기간 필터)
def test_apply_filters_date(sample_df):
    date_range = ["2023-01-01", "2023-01-31"]
    filtered = FinanceLogic.apply_filters(sample_df, date_range, "")
    
    assert len(filtered) == 3  # 1월 데이터만 3개
    assert all(filtered["date"].dt.month == 1)

# 6. FinanceLogic.apply_filters 테스트 (키워드 필터)
def test_apply_filters_keyword(sample_df):
    filtered = FinanceLogic.apply_filters(sample_df, [], "운동화")
    
    assert len(filtered) == 1
    assert filtered.iloc[0]["description"] == "운동화"

# 7. 빈 데이터프레임 처리 테스트 (Edge Case)
def test_calc_summary_empty():
    empty_df = pd.DataFrame(columns=["date", "type", "category", "description", "amount"])
    income, expense, balance = FinanceLogic.calc_summary(empty_df)
    
    assert income == 0
    assert expense == 0
    assert balance == 0