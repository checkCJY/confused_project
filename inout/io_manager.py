# 파일 시스템과의 통신(읽기/쓰기)을 전담합니다.
import pandas as pd
import os


from data import constants
from datetime import datetime


class IOManager:
    def __init__(self, filename="data/data.csv"):
        self.filename = filename
        
        
    def save_transactions(self,transactions, filename="data/data.csv"):
        """거래 데이터를 CSV 파일로 저장"""
        df = pd.DataFrame(
            transactions, columns=constants.COLUMNS)
        df.to_csv(filename, index=False, encoding="utf-8-sig")
        

    def load_transactions(self):
        # CSV 파일에서 데이터를 로드하여 리스트 형식으로 반환
        if os.path.exists(self.filename):
            # try:
            df = pd.read_csv(self.filename, encoding="utf-8-sig")
            if df.empty:
                return []
            # pandas 데이터를 파이썬 리스트 형식으로 변환
            return df[constants.COLUMNS].values.tolist()
            # except Exception:
                # return []
        return []