# 파일 시스템과의 통신(읽기/쓰기)을 전담합니다.
import pandas as pd
import shutil
import os

from datetime import datetime

class IOManager:
    def __init__(self, filename="data.csv"):
        self.filename = filename
        
    def save_transactions(self,transactions, filename="data.csv"):
        """거래 데이터를 CSV 파일로 저장"""
        df = pd.DataFrame(
            transactions, columns=["date", "type", "category", "description", "amount"]
        )
        df.to_csv(filename, index=False, encoding="utf-8-sig")

    def load_transactions(self):
        """CSV 파일에서 데이터를 로드하여 리스트 형식으로 반환"""
        if os.path.exists(self.filename):
            try:
                df = pd.read_csv(self.filename, encoding="utf-8-sig")
                if df.empty:
                    return []
                # pandas 데이터를 파이썬 리스트 형식으로 변환
                return df[["date", "type", "category", "description", "amount"]].values.tolist()
            except Exception:
                return []
        return []
    
    def create_backup(self):
        """현재 data.csv 파일을 복사하여 백업본 생성"""
        if os.path.exists(self.filename):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"data_backup_{timestamp}.csv"
            shutil.copy(self.filename, backup_name) # 파일 복사 로직
            return backup_name
        return None

    def delete_file(self):
        """원본 데이터 파일 삭제 (전체 초기화용)"""
        if os.path.exists(self.filename):
            os.remove(self.filename) # 파일 삭제 로직