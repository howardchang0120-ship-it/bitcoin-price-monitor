
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 網頁設定，只能設定一次
st.set_page_config(
    page_title="比特幣智慧監測站",
    layout="wide"
)

plt.rcParams['font.family'] = 'Microsoft JhengHei'

st.title("₿ 比特幣雲端趨勢與智慧決策平台")

# 從資料庫讀取資料
def load_data():
    conn = sqlite3.connect('crypto_monitor.db')
    df = pd.read_sql_query(
        "SELECT * FROM crypto_trends ORDER BY id DESC LIMIT 15",
        conn
    )
    conn.close()
    return df

df = load_data()

if df.empty:
    st.warning("目前資料庫沒有資料，請先執行資料抓取程式。")
else:
    df['time'] = pd.to_datetime(df['time'])
    df = df.sort_values('time')

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📈 比特幣價格走勢")

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(
            df['time'],
            df['price'],
            marker='o',
            color='orange'
        )
        ax.set_ylabel("價格（美元）")
        ax.set_xlabel("時間")
        ax.grid(True)

        plt.xticks(rotation=45)
        st.pyplot(fig)

    with col2:
        st.success(df['news_and_rule'].iloc[-1])
        st.dataframe(
            df[['time', 'price']],
            hide_index=True
        )

st.write("技術說明：本系統使用 Python 擷取比特幣歷史價格資料，透過 Pandas 進行資料篩選，並利用 If-Then 條件規則，以 96,000 美元為門檻進行價格分類，最後將結果儲存至 SQLite 資料庫。")
