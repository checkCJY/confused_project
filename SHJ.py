import pandas as pd
import streamlit as st

# 1. 클래스 정의
class Transaction:
    def __init__(self, date, ttype, category, description, amount):
        self.date = date
        self.ttype = ttype
        self.category = category
        self.description = description
        self.amount = amount

# 2. CSV 파일 불러오기
file_path = '/root/confused_project/data.csv'

try:
    df_local = pd.read_csv(file_path)
    
    # 3. CSV의 각 행을 Transaction 객체로 변환하여 리스트에 담기
    transaction_list = []
    for index, row in df_local.iterrows():
        # CSV의 컬럼명과 클래스 인자 순서를 맞춰줍니다.
        # 예: CSV 컬럼명이 '날짜', '유형', '카테고리', '내용', '금액'인 경우
        obj = Transaction(
            date=row['date'],
            ttype=row['type'],
            category=row['category'],
            description=row['description'],
            amount=row['amount']
        )
        transaction_list.append(obj)


    for tx in transaction_list:
        if tx.ttype == "지출":
            
      
            st.write(f" 📂 카테고리: {tx.category} | 💰 금액: {tx.amount:,}원")g
    

except FileNotFoundError:
    st.error("파일을 찾을 수 없습니다.")
except KeyError as e:
    st.error(f"CSV 컬럼명이 일치하지 않습니다: {e}")

df = pd.DataFrame(obj)
st.bar_chart(df.set_index("category"))