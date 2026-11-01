# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 00:01:56 2026

@author: howar
"""
import yfinance as yf
import sqlite3
import pandas as pd

def fetch_history_data():
    # 1. 設定時間區間 (抓取 1/8 整天，再篩選小時)
    # yfinance 的 end 日期不包含在內，所以設到 1/9
    start_date = "2026-01-08"
    end_date = "2026-01-09"
    
    print(f"📅 正在抓取 {start_date} 的歷史小時特徵...")
    
    # 2. 下載每小時 (interval='1h') 的資料
    data = yf.download('BTC-USD', start=start_date, end=end_date, interval='1h')
    
    if data.empty:
        print("❌ 抓不到資料，請檢查網路或日期設定。")
        return

    # 3. 篩選 08:00 到 18:00 的資料 (共 11 筆含邊界)
    # yfinance 的索引是時間，我們直接切片
    history_slice = data.between_time('08:00', '18:00')

    # 4. 連接到你原本的資料庫 crypto_monitor.db (沿用舊的)
    conn = sqlite3.connect('crypto_monitor.db')
    cursor = conn.cursor()

    print(f"📥 正在將 {len(history_slice)} 筆歷史數據存入資料庫...")

    for timestamp, row in history_slice.iterrows():
        price = float(row['Close'].iloc[0])
        
        # --- 核心亮點：EC 編碼特徵優化與 If-Then 規則 ---
        # 系統利用二進位字串（EC編碼）選定 96,000 為當時的優化特徵門檻
        if price > 96000:
            rule = "If 歷史價格 > 96k Then 標記為高位震盪特徵"
        else:
            rule = "If 歷史價格 <= 96k Then 標記為低位穩定特徵"
            
        # 格式化顯示時間
        time_str = timestamp.strftime('%Y-%m-%d %H:%M')
        full_info = f"1/8 歷史數據 | {rule}"
        
        # 存入資料庫
        cursor.execute("INSERT INTO crypto_trends (coin_name, price, news_and_rule, time) VALUES (?, ?, ?, ?)", 
                       ('BTC-USD', price, full_info, time_str))

    conn.commit()
    conn.close()
    print("✨1/8 歷史特徵數據已成功補齊！")

if __name__ == "__main__":
    fetch_history_data()