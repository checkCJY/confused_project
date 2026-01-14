# 데이터 객체 생성, 전처리, 합계 계산 등 핵심 규칙을 담당합니다.
import pandas as pd
from data import constants


class Transaction:
    # 거래 데이터를 생성하고 리스트로 출력하는 클래스
    def __init__(self, date, ttype, category, description, amount):
        self.date = date
        self.ttype = ttype
        self.category = category
        self.description = description
        self.amount = amount

    def output(self):
        return [self.date, self.ttype, self.category, self.description, self.amount]


class FinanceLogic:
    @staticmethod
    def process_dataframe(history):
        # 리스트 데이터를 판다스 데이터프레임으로 변환 및 날짜 타입 최적화
        df = pd.DataFrame(history, columns=constants.COLUMNS)  # 이런식으로 수정
        df["date"] = pd.to_datetime(df["date"])
        return df

    @staticmethod
    def calc_summary(df):
        # 데이터프레임 기준 수입, 지출 합계 및 잔액 계산
        income = df[df["type"] == constants.TYPE_INCOME]["amount"].sum()
        expense = df[df["type"] == constants.TYPE_EXPENSE]["amount"].sum()
        balance = income - expense
        return income, expense, balance

    @staticmethod
    def apply_filters(df, date_range, keyword):
        # 기간 및 키워드 기준 데이터 필터링
        filtered = df.copy()
        if len(date_range) == 2:
            filtered = filtered[
                filtered["date"].between(
                    pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
                )
            ]
        if keyword:
            filtered = filtered[
                filtered["description"].str.contains(keyword, case=False, na=False)
            ]
        return filtered
