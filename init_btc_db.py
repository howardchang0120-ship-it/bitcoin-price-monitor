# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sqlite3

def init_db():
    conn = sqlite3.connect('crypto_monitor.db')
    cursor = conn.cursor()
    # 建立表格：包含 ID、幣別、價格
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS crypto_trends (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        coin_name TEXT,
        price REAL,
        news_and_rule TEXT,
        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()
    print("比特幣資料庫初始化成功！")

if __name__ == "__main__":
    init_db()
    