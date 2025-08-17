import os
import psycopg2
import pandas as pd

def get_station_data(station, start_date, end_date):
    try:
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port=os.getenv("PORT", "5432")
        )

        query = """
        SELECT r."日期", s."stationName", r."進站人數", r."出站人數"
        FROM "每日各站進出站人數" r
        JOIN "台鐵車站資訊" s
          ON s."stationName" = %s
          AND r."車站代碼" = s."stationCode"
        WHERE r."日期" BETWEEN %s AND %s;
        """
        df = pd.read_sql(query, conn, params=(station, start_date, end_date))

        return df

    except psycopg2.Error as e:
        print(f"資料庫連線或查詢失敗：{e}")
        return None
    except Exception as e:
        print(f"發生未預期的錯誤：{e}")
        return None
    finally:
        if 'conn' in locals():
            conn.close()
